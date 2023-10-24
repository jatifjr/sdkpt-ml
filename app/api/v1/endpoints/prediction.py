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


@router.get("/real-data/id={id}")
async def get_real_data_by_id(id: int = Path(..., title="ID of Kelurahan")):
    real_data = service.get_real_data_by_id(id)
    if not real_data:
        raise HTTPException(status_code=404, detail="ID not found")
    return real_data


@router.get("/predicted-data/id={id}")
async def get_predicted_data_by_id(id: int = Path(..., title="ID of Kelurahan")):
    predicted_data = service.get_predicted_data_by_id(id)
    if not predicted_data:
        raise HTTPException(status_code=404, detail="ID not found")
    return predicted_data
