from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.patient import PatientResponse
from app.crud.patient import patient

router = APIRouter()


@router.get("/{kelurahan_id}", response_model=List[PatientResponse])
def get_patients_by_kelurahan(
    kelurahan_id: int,
    page: int = Query(1, ge=1),  # Default to 1, must be greater or equal to 1
    limit: int = Query(10, gt=0),  # Default to 10, must be greater than 0
    db: Session = Depends(deps.get_db),
):
    skip = (page - 1) * limit
    patients = patient.get_by_kelurahan_id(
        db, kelurahan_id, skip=skip, limit=limit)
    if not patients:
        raise HTTPException(
            status_code=404, detail="No patients found for the given kelurahan_id")
    return patients
