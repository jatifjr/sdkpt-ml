from fastapi import APIRouter

from .routes import (
    intervention,
    survey
)

api_router = APIRouter()
api_router.include_router(
    intervention.router, prefix="/interventions", tags=["interventions"])
api_router.include_router(survey.router, prefix="/surveys", tags=["surveys"])
