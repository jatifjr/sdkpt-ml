from fastapi import APIRouter

from .routes import (
    kelurahan,
    intervention,
    survey,
    cases,
    prediction,
    vulnerability,
    semar_betul,
    patient,
    upload_survey
)

api_router = APIRouter()
api_router.include_router(
    kelurahan.router, prefix="/kelurahan", tags=["ref kelurahan"])
api_router.include_router(
    intervention.router, prefix="/interventions", tags=["interventions"])
api_router.include_router(survey.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(cases.router, tags=["cases"])
api_router.include_router(
    prediction.router, tags=["predictions"])
api_router.include_router(vulnerability.router, tags=["vulnerabilities"])
api_router.include_router(
    semar_betul.router, prefix="/semar-betul", tags=["semar_betul"])
api_router.include_router(
    patient.router, prefix="/patients", tags=["patients"])
api_router.include_router(upload_survey.router,
                          prefix="/upload", tags=["upload survey"])
