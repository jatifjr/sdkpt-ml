from fastapi import APIRouter, Depends
from typing import Dict
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.crud.patient import patient
from app.schemas.cases import CasesResponse

router = APIRouter()


@router.get("/cases/id={kelurahan_id}", response_model=CasesResponse)
def get_case_count_by_kelurahan_id(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db)
):
    case_count = patient.get_case_and_outcome_counts(db, kelurahan_id)
    return {"jumlah_kasus": case_count.jumlah_kasus}
