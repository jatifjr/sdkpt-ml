import time
from typing import List, Union, Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.utils.semar_betul import ApiClient
from app.core.config import settings
from app.schemas.semar_betul_auth import SemarBetulAuth
from app.schemas.patient import PatientResponse
from app.crud.patient import CRUDPatient

router = APIRouter()


# ! DO NOT TOUCH ALL OF THIS

@router.get("/test-access-token", response_model=SemarBetulAuth)
def test_access_token(db: Session = Depends(deps.get_db)):
    # Initialize ApiClient with base URL, username, password, and database session
    base_url = settings.SB_BASE_URL
    username = settings.SB_USERNAME
    password = settings.SB_PASSWORD

    api_client = ApiClient(base_url, db)

    # Attempt to login and fetch access token
    access_token = api_client.login(username, password)
    if access_token:
        return SemarBetulAuth(access_token=access_token)
    else:
        raise HTTPException(
            status_code=500, detail="Failed to fetch access token")


@router.get("/fetch-patient-data", response_model=Union[List[PatientResponse], Dict[str, str]])
def fetch_patient_data(
    db: Session = Depends(deps.get_db),
    page: int = 1,
):
    base_url = settings.SB_BASE_URL
    username = settings.SB_USERNAME
    password = settings.SB_PASSWORD

    api_client = ApiClient(base_url, db)
    access_token = api_client.login(username, password)
    if page < 1:
        raise HTTPException(
            status_code=400, detail="Invalid number of pages to fetch")

    patient_data = api_client.fetch_patient_data(access_token, page)
    if patient_data is None:
        raise HTTPException(
            status_code=500, detail="Failed to fetch patient data")

    return patient_data


@router.post("/trigger-fetch-patient-data", response_model=List[PatientResponse])
def trigger_fetch_patient_data(
    db: Session = Depends(deps.get_db),
):
    base_url = settings.SB_BASE_URL
    username = settings.SB_USERNAME
    password = settings.SB_PASSWORD

    api_client = ApiClient(base_url, db)
    access_token = api_client.login(username, password)
    all_patient_data = []
    page = 845

    while True:
        patient_data = api_client.fetch_patient_data(access_token, page)

        if patient_data is None:
            raise HTTPException(
                status_code=500, detail=f"Failed to fetch patient data"
            )
        elif isinstance(patient_data, list) and patient_data:
            all_patient_data.extend(patient_data)
            page += 1
        elif isinstance(patient_data, dict) and patient_data.get("status") == "OK":
            break  # Stop if all patient data already fetched

        # Wait for 1.2 seconds between each request to limit to 50 requests per minute
        time.sleep(1.2)

        # Renew the access token after every 50 pages
        if page % 50 == 0:
            access_token = api_client.login(username, password)

    return all_patient_data
