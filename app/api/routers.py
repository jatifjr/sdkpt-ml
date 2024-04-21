from fastapi import APIRouter

from .routes import (
    intervention,
    survey,
    cases,
    prediction,
    vulnerability,
)

api_router = APIRouter()
api_router.include_router(
    intervention.router, prefix="/interventions", tags=["interventions"])
api_router.include_router(survey.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(cases.router, tags=["cases"])
api_router.include_router(
    prediction.router, tags=["predictions"])
api_router.include_router(vulnerability.router, tags=["vulnerabilities"])
