from fastapi import APIRouter, Path
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from typing import List
import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from app.service.prediction_service import ForecastService


router = APIRouter()
service = ForecastService()


@router.get("/forecast/id={id}")
async def get_forecast_id(id: int = Path(..., title="ID of Kelurahan")):
    # Call the service to get the forecast by 'id'
    recharts_data = service.get_forecast_by_id(id)
    if recharts_data is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return recharts_data
