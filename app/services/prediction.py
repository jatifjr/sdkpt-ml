from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import logging
import pickle
import os

from app.db.session import engine
from app.models.kelurahan import Kelurahan
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class ForecastService:
    def __init__(self):
        # Fetch data from MySQL and prepare the dataset
        query = ('SELECT kelurahan_domisili, tahun, bulan, COUNT(*) as patient_count '
                 'FROM patient GROUP BY kelurahan_domisili, tahun, bulan')
        df = pd.read_sql(query, engine)

        # Filter out invalid 'tahun' and 'bulan' entries
        df = df.dropna(subset=['tahun', 'bulan'])
        df['tahun'] = df['tahun'].astype(int)
        df['bulan'] = df['bulan'].astype(int)
        df = df[(df['tahun'] > 0) & (df['bulan'] > 0)]

        # Convert 'tahun' and 'bulan' to datetime
        try:
            df['date'] = pd.to_datetime(df['tahun'].astype(
                str) + '-' + df['bulan'].astype(str) + '-01')
        except Exception as e:
            logger.error(
                f"Error converting 'tahun' and 'bulan' to datetime: {str(e)}")
            raise

        df.set_index('date', inplace=True)
        df.drop(columns=['tahun', 'bulan'], inplace=True)

        # Filter out years in the past with no patient count
        min_year_threshold = 2015
        df = df[df.index.year >= min_year_threshold]

        # Filter out unrealistic future dates
        max_year_threshold = datetime.now().year + 1  # 1 year from now
        df = df[df.index.year <= max_year_threshold]

        # Filter out future dates and find the maximum date in the dataset
        current_date = datetime.now().replace(day=1).date()  # First day of current month
        max_date_in_dataset = df.index.max().date()

        # Set the end date for predictions to 1 year from the current date or the max date in the dataset
        end_date = min(current_date.replace(
            year=current_date.year + 1), max_date_in_dataset)

        # Pivot the table to have one column per 'kelurahan_domisili' and integer values
        pivot_df = df.pivot_table(index='date', columns='kelurahan_domisili',
                                  values='patient_count', aggfunc=np.sum, fill_value=0)

        # Filter out columns with invalid 'kelurahan_domisili' values
        valid_columns = pivot_df.columns[pivot_df.columns.str.contains(
            r'^[Kk][Dd]\d+|^xxx$')]
        pivot_df = pivot_df[valid_columns]

        # Assign pivot_df to self
        self.pivot_df = pivot_df

        # Create a directory to store the models
        self.model_dir = 'models'
        if not os.path.exists(self.model_dir):
            os.makedirs(self.model_dir)

    def get_kelurahan_series(self, db: Session, kelurahan_id):
        # Fetch the kelurahan with the given id
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            raise ValueError(f"Kelurahan with id '{kelurahan_id}' not found.")

        kelurahan_domisili = kelurahan.kode_kd

        if kelurahan_domisili in self.pivot_df.columns:
            return self.pivot_df[kelurahan_domisili]
        else:
            raise ValueError(
                f"Kelurahan '{kelurahan_domisili}' not found in the dataset.")

    def train_sarima_model(self, series, kelurahan_id):
        model_file = os.path.join(self.model_dir, f'{kelurahan_id}.pkl')
        logger.info(f"Training model for kelurahan_id {kelurahan_id}")
        model = SARIMAX(series, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        results = model.fit(disp=False)
        with open(model_file, 'wb') as f:
            pickle.dump(results, f)
        logger.info(
            f"Model for kelurahan_id {kelurahan_id} saved to {model_file}")
        return results

    def load_model(self, kelurahan_id):
        model_file = os.path.join(self.model_dir, f'{kelurahan_id}.pkl')
        if not os.path.exists(model_file):
            raise ValueError(
                f"Model for kelurahan_id '{kelurahan_id}' not found.")
        with open(model_file, 'rb') as f:
            results = pickle.load(f)
        return results

    def get_predicted_data_by_id(self, db: Session, kelurahan_id: int):
        series = self.get_kelurahan_series(db, kelurahan_id)

        # Load or train the model
        try:
            model_fit = self.load_model(kelurahan_id)
        except ValueError:
            model_fit = self.train_sarima_model(series, kelurahan_id)

        # Generate a list of future months
        if not isinstance(series.index, pd.DatetimeIndex):
            series.index = pd.to_datetime(series.index)

        # Calculate start and end dates
        current_date = datetime.now().replace(day=1).date()  # First day of current month
        start_date = current_date - timedelta(days=2 * 365)  # 2 years ago
        end_date = current_date.replace(
            year=current_date.year + 1)  # 1 year from now

        # Predict values for the future months
        future_months = pd.date_range(start=start_date, end=end_date, freq='M')
        future_predictions = model_fit.get_forecast(steps=len(future_months))

        # Concatenate historical and predicted data
        combined_data = pd.concat(
            [series, future_predictions.predicted_mean.rename('Value')])

        # Round the predictions and convert to integers
        combined_data = combined_data.round().astype(int)

        # Clip values to ensure they are not below 0
        combined_data = np.maximum(combined_data, 0)

        # Filter out data within the desired range
        combined_data = combined_data[(combined_data.index >= pd.Timestamp(
            start_date)) & (combined_data.index <= pd.Timestamp(end_date))]

        # Convert predicted data to a list of dictionaries with formatted date strings
        predicted_data = [{"Month": self.format_month_year(date), "PredictedValue": int(value)}
                          for date, value in combined_data.items()]

        return predicted_data

    def format_month_year(self, date):
        return date.strftime("%b %Y")

    def get_actual_data_by_id(self, db: Session, kelurahan_id: int):
        series = self.get_kelurahan_series(db, kelurahan_id)

        # Filter out data within the desired range (last 5 years until now)
        current_date = datetime.now().replace(day=1).date()  # First day of current month
        start_date = current_date - timedelta(days=2 * 365)  # 5 years ago

        # Filter actual data
        actual_data = series[series.index >= pd.Timestamp(start_date)]

        # Convert actual data to a list of dictionaries with formatted date strings
        actual_data_formatted = [{"Month": self.format_month_year(date), "RealValue": int(value)}
                                 for date, value in actual_data.items()]

        return actual_data_formatted


forecast_service = ForecastService()
