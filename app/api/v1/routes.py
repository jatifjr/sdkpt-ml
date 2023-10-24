from fastapi import APIRouter

from app.api.v1.endpoints import root, prediction

api_router = APIRouter()

# api_router.include_router(root.router, tags=["root"])
api_router.include_router(prediction.router, tags=["forecast"])
