from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.config import settings
from app.api import deps
from app.schemas.patient import PatientCaseAndOutcomeCounts, TotalCasesAndOutcomesResponse
from app.utils.semar_betul import ApiClient
from app.crud import patient

router = APIRouter()


@router.get("/kelurahan", response_model=PatientCaseAndOutcomeCounts)
def get_case_and_outcome_counts(kelurahan_id: int, db: Session = Depends(deps.get_db)):
    counts = patient.get_case_and_outcome_counts(db, kelurahan_id)
    return counts


@router.get("/all", response_model=TotalCasesAndOutcomesResponse)
def get_total_cases_and_outcomes(background_tasks: BackgroundTasks, db: Session = Depends(deps.get_db)):
    base_url = settings.SB_BASE_URL
    username = settings.SB_USERNAME
    password = settings.SB_PASSWORD

    api_client = ApiClient(base_url, db)
    access_token = api_client.login(username, password)

    # Start fetching patient data in the background
    background_tasks.add_task(
        api_client.fetch_patient_data, access_token=access_token)

    counts = patient.get_total_cases_and_outcomes(db)
    return counts
