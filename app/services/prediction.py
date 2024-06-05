from app.models.patient import Patient  # Import the Patient model
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from app.db.session import engine
from app.models.kelurahan import Kelurahan
from sqlalchemy.orm import Session
import logging
import pickle
import os
import numpy as np
from datetime import datetime

logger = logging.getLogger(__name__)


# app/services/prediction.py


logger = logging.getLogger(__name__)


class ForecastService:
    def __init__(self):
        # Fetch data from MySQL and prepare the dataset
        query = ('SELECT kelurahan_domisili, tahun, bulan, COUNT(*) as patient_count '
                 'FROM patient GROUP BY kelurahan_domisili, tahun, bulan')
        df = pd.read_sql(query, engine)

        # Filter out invalid 'tahun' and 'bulan' entries
        # Drop rows with NaN in tahun or bulan
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

        # Filter out future dates
        current_date = datetime.now().replace(day=1).date()  # First day of current month
        df = df[df.index.date <= current_date]

        # Filter out years in the past with no patient count
        min_year_threshold = 2015
        df = df[df.index.year >= min_year_threshold]

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
        # Fetch the kelurahan with the given id
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            raise ValueError(f"Kelurahan with id '{kelurahan_id}' not found.")

        kelurahan_domisili = kelurahan.kode_kd

        if kelurahan_domisili in self.pivot_df.columns:
            data = self.pivot_df[kelurahan_domisili]
        else:
            raise ValueError(
                f"Kelurahan '{kelurahan_domisili}' not found in the dataset.")

        # Define SARIMA orders
        p, d, q = 5, 1, 0  # Example order; adjust as needed
        P, D, Q, S = 1, 1, 1, 12  # Example seasonal order; adjust as needed

        # Fit the SARIMA model
        model = SARIMAX(data, order=(p, d, q), seasonal_order=(P, D, Q, S))
        model_fit = model.fit(disp=False)

        # Generate a list of future months
        start_date = data.index.max() + pd.DateOffset(months=1)
        end_date = datetime.now().replace(
            day=1).date() + pd.DateOffset(months=12)
        future_months = pd.date_range(
            start=start_date, end=end_date, freq='M')

        # Predict values for the future months
        future_predictions = model_fit.get_forecast(
            steps=len(future_months) - len(data))

        # Concatenate historical and predicted data
        combined_data = pd.concat(
            [data, future_predictions.predicted_mean.rename('Value')])

        # Round the predictions and convert to integers
        combined_data = combined_data.round().astype(int)

        # Clip values to ensure they are not below 0
        combined_data = np.maximum(combined_data, 0)

        # Convert predicted data to a list of dictionaries with formatted date strings
        predicted_data = [{"Month": self.format_month_year(date), "PredictedValue": int(value)}
                          for date, value in combined_data.items()]

        return predicted_data

    def format_month_year(self, date):
        return date.strftime("%b %Y")


forecast_service = ForecastService()
