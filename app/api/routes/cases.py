from fastapi import APIRouter, Path
from fastapi.exceptions import HTTPException
from app.services.case_service import CaseService


router = APIRouter()

service = CaseService()


@router.get("/cases/id={id}")
async def get_cases_by_id(id: int = Path(..., title="ID of Kelurahan")):
    cases_data = service.get_cases_by_id(id)
    if cases_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return cases_data
