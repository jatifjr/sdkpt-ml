from fastapi import APIRouter

from app.api.v1.endpoints import root, prediction, vulnerability

api_router = APIRouter()

# api_router.include_router(root.router, tags=["root"])
api_router.include_router(prediction.router, tags=["forecast"])
api_router.include_router(vulnerability.router, tags=["vulnerability"])
