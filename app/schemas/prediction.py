from pydantic import BaseModel
from typing import List
from datetime import date


class TrainRequest(BaseModel):
    kelurahan_id: int


class ForecastRequest(BaseModel):
    kelurahan_id: int
    periods: int = 12


class ForecastResponse(BaseModel):
    dates: List[date]
    predictions: List[float]


class RealDataResponse(BaseModel):
    Month: str
    RealValue: float
