from fastapi import APIRouter, Path
from fastapi.exceptions import HTTPException
from app.service.intervention_service import IntervensiService

router = APIRouter()
service = IntervensiService()


@router.get("/intervention/id={id}")
async def get_intervention_by_id(id: int = Path(..., title="ID of Kelurahan")):
    intervention_data = service.get_intervention_by_id(id)
    if not intervention_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return intervention_data
