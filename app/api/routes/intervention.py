from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.crud.intervention import InterventionService

router = APIRouter()
intervention_crud = InterventionService()


@router.get("/{intervention_id}/list", response_model=List[schemas.InterventionResponseBody])
def read_intervention_response_by_id(
    intervention_id: int,
    db: Session = Depends(deps.get_db)
):
    intervention = intervention_crud.get_by_kelurahan_id(db, intervention_id)
    if not intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")

    intervention_responses = [
        {"isi_intervensi": getattr(intervention, f'intervention_{i}')}
        for i in range(1, 8)
        if getattr(intervention, f'intervention_{i}')
    ]

    return intervention_responses
