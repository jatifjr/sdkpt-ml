from fastapi import APIRouter, Path, Depends
from fastapi.exceptions import HTTPException
from app.services.prediction_service import ForecastService
from app.services.prediction import forecast_service
# from app.services.pred import forecast_service
from app.schemas.prediction import TrainRequest, ForecastRequest, ForecastResponse, RealDataResponse
from sqlalchemy.orm import Session
from app.api import deps
import logging
from typing import List
import pandas as pd


logger = logging.getLogger(__name__)

router = APIRouter()
service = ForecastService()


# ! DO NOT TOUCH THIS
@router.get("/real-data/id={kelurahan_id}", response_model=List[RealDataResponse])
def get_kelurahan_series(kelurahan_id: int, db: Session = Depends(deps.get_db)):
    try:
        real_data = forecast_service.get_kelurahan_series(db, kelurahan_id)

        # Ensure index is DatetimeIndex
        if not isinstance(real_data.index, pd.DatetimeIndex):
            real_data.index = pd.to_datetime(real_data.index)

        # Transform the Month format
        real_data.index = real_data.index.strftime('%b %Y')

        # Convert Series to a list of dictionaries
        response_data = [
            # Ensure RealValue is integer
            {"Month": month, "RealValue": int(value)}
            for month, value in zip(real_data.index, real_data.values)
        ]

        return response_data

    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))


# @router.get("/real-data/id={kelurahan_id}")
# def get_real_data(kelurahan_id: int = Path(..., title="ID of Kelurahan")):
#     real_data = service.get_real_data_by_id(kelurahan_id)
#     if not real_data:
#         raise HTTPException(status_code=404, detail="ID not found")
#     return real_data


@router.get("/predicted-data/id={id}")
async def get_predicted_data_by_id(id: int = Path(..., title="ID of Kelurahan")):
    predicted_data = service.get_predicted_data_by_id(id)
    if not predicted_data:
        raise HTTPException(status_code=404, detail="ID not found")
    return predicted_data


# @router.post("/train")
# def train(request: TrainRequest, db: Session = Depends(deps.get_db)):
#     try:
#         kelurahan_series = forecast_service.get_kelurahan_series(
#             db, request.kelurahan_id)
#         forecast_service.train_sarima_model(
#             kelurahan_series, request.kelurahan_id)
#         return {"message": f"Model for kelurahan_id {request.kelurahan_id} trained successfully."}
#     except ValueError as e:
#         logger.error(
#             f"Error training model for kelurahan_id {request.kelurahan_id}: {e}")
#         raise HTTPException(status_code=404, detail=str(e))

# @router.post("/train")
# def train(db: Session = Depends(deps.get_db)):
#     try:
#         # Train the SARIMA model using the pivot table from forecast_service
#         forecast_service.train_sarima_model()
#         return {"message": "SARIMA model trained successfully for all kelurahan."}
#     except Exception as e:
#         logger.error(f"Error training SARIMA model: {e}")
#         raise HTTPException(
#             status_code=500, detail="An error occurred while training the SARIMA model.")


# @router.post("/forecast", response_model=ForecastResponse)
# def forecast(request: ForecastRequest, db: Session = Depends(deps.get_db)):
#     try:
#         predictions = forecast_service.forecast(
#             db, request.kelurahan_id, request.periods)
#         logger.info(
#             f"Forecasts for kelurahan_id {request.kelurahan_id}: {predictions}")

#         return ForecastResponse(
#             dates=predictions.index.strftime('%Y-%m-%d').to_list(),
#             predictions=predictions.to_list()
#         )
#     except ValueError as e:
#         logger.error(
#             f"Error forecasting for kelurahan_id {request.kelurahan_id}: {e}")
#         raise HTTPException(status_code=404, detail=str(e))
#     except KeyError as e:
#         logger.error(
#             f"KeyError in forecasting for kelurahan_id {request.kelurahan_id}: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")
