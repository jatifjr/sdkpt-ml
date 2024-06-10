# prediction_service.py
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import datetime
import numpy as np


# ! DO NOT TOUCH ALL OF THIS
class ForecastService:
    def __init__(self):
        # Load your data with correct delimiters
        self.df = pd.read_csv('app/data/monthly_cases.csv', sep=',')
        self.mapping_df = pd.read_csv(
            'app/data/kelurahan_monthly.csv')  # Load the mapping data

    def format_month_year(self, date):
        return datetime.strftime(date, '%b %Y')

    def get_real_data_by_id(self, id: int):
        # Find 'nama_kelurahan' based on 'id' from the mapping data
        nama_kelurahan = self.mapping_df.loc[self.mapping_df['id']
                                             == id, 'nama_kelurahan'].values[0]

        # Extract the data for the specified 'nama_kelurahan'
        data = self.df[self.df['Kelurahan Pasien'] == nama_kelurahan]

        # Remove the "Kelurahan Pasien" column
        data = data.drop(columns='Kelurahan Pasien')

        # Transpose the DataFrame
        data = data.transpose()
        data.columns = ['Value']

        # Reset the index and format the 'Month' column as datetime
        data.reset_index(inplace=True)
        data.rename(columns={'index': 'Month'}, inplace=True)
        data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m')

        # Set the 'Month' column as the index
        data.set_index('Month', inplace=True)

        # Convert real data to a list of dictionaries with formatted date strings
        real_data = [{"Month": self.format_month_year(date), "RealValue": real_value}
                     for date, real_value in zip(data.index, data['Value'])]

        return real_data

    def get_predicted_data_by_id(self, id: int):
        # Find 'nama_kelurahan' based on 'id' from the mapping data
        nama_kelurahan = self.mapping_df.loc[self.mapping_df['id']
                                             == id, 'nama_kelurahan'].values[0]

        # Extract the data for the specified 'nama_kelurahan'
        data = self.df[self.df['Kelurahan Pasien'] == nama_kelurahan]

        # Remove the "Kelurahan Pasien" column
        data = data.drop(columns='Kelurahan Pasien')

        # Transpose the DataFrame
        data = data.transpose()
        data.columns = ['Value']

        # Reset the index and format the 'Month' column as datetime
        data.reset_index(inplace=True)
        data.rename(columns={'index': 'Month'}, inplace=True)
        data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m')

        # Set the 'Month' column as the index
        data.set_index('Month', inplace=True)

        # Define SARIMA orders
        p, d, q = 5, 1, 0  # Example order; adjust as needed
        P, D, Q, S = 1, 1, 1, 12  # Example seasonal order; adjust as needed

        # Fit the SARIMA model
        model = SARIMAX(data, order=(p, d, q), seasonal_order=(P, D, Q, S))
        model_fit = model.fit(disp=False)

        # Generate a list of future months
        start_date = pd.to_datetime('2018-01-01', format='%Y-%m-%d')
        end_date = datetime.now().replace(day=1).date() - pd.DateOffset(months=12)
        future_months = pd.date_range(
            start=start_date, end=end_date, freq='M')

        # Predict values for the future months
        future_predictions = model_fit.get_forecast(
            steps=len(future_months) - len(data))

        # Concatenate historical and predicted data
        combined_data = pd.concat(
            [data['Value'], future_predictions.predicted_mean.rename('Value')])

        # Round the predictions and convert to integers
        combined_data = combined_data.round().astype(int)

        # Clip values to ensure they are not below 0
        combined_data = np.maximum(combined_data, 0)

        # Convert predicted data to a list of dictionaries with formatted date strings
        predicted_data = [{"Month": self.format_month_year(date), "PredictedValue": value}
                          for date, value in combined_data.items()]

        return predicted_data
