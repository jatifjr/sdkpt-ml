# import pandas as pd
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# from app.db.session import engine
# from app.models.kelurahan import Kelurahan
# from sqlalchemy.orm import Session
# import logging
# import pickle
# import os
# import numpy as np
# from datetime import datetime

# logger = logging.getLogger(__name__)


# class ForecastService:
#     def __init__(self):
#         # Fetch data from MySQL and prepare the dataset
#         query = ('SELECT kelurahan_domisili, tahun, bulan, COUNT(*) as patient_count '
#                  'FROM patient GROUP BY kelurahan_domisili, tahun, bulan')
#         df = pd.read_sql(query, engine)

#         # Filter out invalid 'tahun' and 'bulan' entries
#         df = df[(df['tahun'] > 0) & (df['bulan'] > 0)]

#         # Convert 'tahun' and 'bulan' to datetime
#         df['date'] = pd.to_datetime(df['tahun'].astype(
#             str) + '-' + df['bulan'].astype(str) + '-01')
#         df.set_index('date', inplace=True)
#         df.drop(columns=['tahun', 'bulan'], inplace=True)

#         # Filter out future dates
#         current_date = datetime.now().replace(day=1).date()  # First day of current month
#         df = df[df.index.date <= current_date]

#         # Filter out years in the past with no patient count
#         min_year_threshold = 2015
#         df = df[df.index.year >= min_year_threshold]

#         # Pivot the table to have one column per 'kelurahan_domisili' and integer values
#         pivot_df = df.pivot_table(index='date', columns='kelurahan_domisili',
#                                   values='patient_count', aggfunc=np.sum, fill_value=0)

#         # Filter out columns with invalid 'kelurahan_domisili' values
#         valid_columns = pivot_df.columns[pivot_df.columns.str.contains(
#             r'^[Kk][Dd]\d+|^xxx$')]
#         pivot_df = pivot_df[valid_columns]

#         # Assign pivot_df to self
#         self.pivot_df = pivot_df

#         # Create a directory to store the model
#         self.model_file = 'ml-models/sarima_model.pkl'

#         # Train the SARIMA model using the sum of all series as the endogenous variable
#         self.train_sarima_model()

#     def train_sarima_model(self):
#         # Use the sum of all series as the endogenous variable
#         endog = self.pivot_df.sum(axis=1)
#         exog = self.pivot_df  # Use the entire pivot_df as the exogenous variables
#         model = SARIMAX(endog, exog=exog, order=(
#             1, 1, 1), seasonal_order=(1, 1, 1, 12))
#         self.model = model.fit(disp=False)

#         # Save the trained model
#         with open(self.model_file, 'wb') as f:
#             pickle.dump(self.model, f)
#         logger.info(f"Model saved to {self.model_file}")

#     def load_model(self):
#         with open(self.model_file, 'rb') as f:
#             self.model = pickle.load(f)
#         logger.info(f"Model loaded from {self.model_file}")

#     def forecast(self, kelurahan_domisili, steps=12):
#         if not hasattr(self, 'model'):
#             self.load_model()

#         # Get exogenous data for the specified kelurahan_domisili
#         if kelurahan_domisili not in self.pivot_df.columns:
#             raise ValueError(
#                 f"Kelurahan '{kelurahan_domisili}' not found in the dataset.")

#         exog = self.pivot_df[kelurahan_domisili].to_frame()

#         # Forecast with the SARIMA model
#         forecast = self.model.get_forecast(steps=steps, exog=exog)
#         forecast_mean = forecast.predicted_mean
#         forecast_ci = forecast.conf_int()

#         # Prepare the response in the desired format
#         forecast_df = pd.DataFrame({
#             'Month': forecast_mean.index.strftime('%b %Y'),
#             'ForecastValue': forecast_mean.values.round().astype(int),
#             'LowerCI': forecast_ci.iloc[:, 0].values.round().astype(int),
#             'UpperCI': forecast_ci.iloc[:, 1].values.round().astype(int)
#         })

#         return forecast_df.to_dict(orient='records')


# # Initialize the ForecastService
# forecast_service = ForecastService()
