# service.py
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX


class ForecastService:
    def __init__(self):
        # Load your data with correct delimiters
        self.df = pd.read_csv('app/data/monthly_cases.csv', sep=',')
        self.mapping_df = pd.read_csv(
            'app/data/kelurahan_monthly.csv')  # Load the mapping data

    def get_forecast_by_id(self, id: int):
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
        start_date = data.index.min()
        end_date = data.index.max()
        future_months = pd.date_range(
            start=start_date, periods=len(data) + 12, freq='M')

        # Predict values for the future months
        future_predictions = model_fit.get_forecast(steps=len(future_months))

        # Extract the real data
        real_data = data.copy()

        # Create a list of dictionaries for Recharts format with real and predicted values
        recharts_data = [{"Month": str(date), "RealValue": real_value, "PredictedValue": predicted_value}
                         for date, real_value, predicted_value in zip(future_months, real_data['Value'], future_predictions.predicted_mean)]

        return recharts_data
