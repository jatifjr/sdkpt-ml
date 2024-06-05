from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.patient import PatientCaseAndOutcomeCounts, TotalCasesAndOutcomesResponse
from app.crud import patient

router = APIRouter()


@router.get("/kelurahan", response_model=PatientCaseAndOutcomeCounts)
def get_case_and_outcome_counts(kelurahan_id: int, db: Session = Depends(deps.get_db)):
    counts = patient.get_case_and_outcome_counts(db, kelurahan_id)
    return counts


@router.get("/all", response_model=TotalCasesAndOutcomesResponse)
def get_total_cases_and_outcomes(db: Session = Depends(deps.get_db)):
    counts = patient.get_total_cases_and_outcomes(db)
    return counts
