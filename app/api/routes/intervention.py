from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps
from app.crud import intervention as intervention_crud

router = APIRouter()


@router.get("/", response_model=List[schemas.InterventionResponse])
def read_interventions(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 10
):
    interventions = intervention_crud.get_multi(db, skip=skip, limit=limit)
    return [schemas.InterventionResponse.from_db(intervention) for intervention in interventions]


# @router.post("/", response_model=schemas.InterventionResponse)
# def create_intervention(
#     *,
#     db: Session = Depends(deps.get_db),
#     intervention_in: schemas.InterventionCreate
# ):
#     intervention = intervention_crud.create(db, obj_in=intervention_in)
#     return schemas.InterventionResponse.from_db(intervention)


@router.get("/{intervention_id}", response_model=schemas.InterventionResponse)
def read_intervention_by_id(
    intervention_id: int,
    db: Session = Depends(deps.get_db)
):
    intervention = intervention_crud.get_by_id(db, intervention_id)
    if not intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")
    return schemas.InterventionResponse.from_db(intervention)


@router.get("/{intervention_id}/list", response_model=List[schemas.InterventionResponseBody])
def read_intervention_response_by_id(
    intervention_id: int,
    db: Session = Depends(deps.get_db)
):
    intervention = intervention_crud.get_by_id(db, intervention_id)
    if not intervention:
        raise HTTPException(status_code=404, detail="Intervention not found")

    intervention_responses = [
        {"isi_intervensi": getattr(intervention, f'intervention_{i}')}
        for i in range(1, 8)
        if getattr(intervention, f'intervention_{i}')
    ]

    return intervention_responses


# @router.put("/{intervention_id}", response_model=schemas.InterventionResponse)
# def update_intervention(
#     *,
#     db: Session = Depends(deps.get_db),
#     intervention_id: int,
#     intervention_in: schemas.InterventionUpdate
# ):
#     intervention = intervention_crud.get(db, id=intervention_id)
#     if not intervention:
#         raise HTTPException(status_code=404, detail="Intervention not found")
#     updated_intervention = intervention_crud.update(
#         db, db_obj=intervention, obj_in=intervention_in)
#     return schemas.InterventionResponse.from_db(updated_intervention)


# @router.delete("/{intervention_id}", response_model=Dict[str, str])
# def delete_intervention(
#     *,
#     db: Session = Depends(deps.get_db),
#     intervention_id: int
# ):
#     intervention = intervention_crud.get(db, id=intervention_id)
#     if not intervention:
#         raise HTTPException(status_code=404, detail="Intervention not found")
#     intervention_crud.remove(db, id=intervention_id)
#     return {"message": "Intervention deleted"}
