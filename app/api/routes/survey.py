from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import upload_survey as crudsurvey
from app.crud import kelurahan as crudkelurahan
from app.schemas import upload_survey


router = APIRouter()


# ! DO NOT TOUCH THIS
@router.get("/kelurahan/latest", response_model=upload_survey.SurveyItem)
def get_latest_kelurahan(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db),
):
    # Retrieve kelurahan name
    kelurahan_name = crudsurvey.get_kelurahan_name_by_id(db, kelurahan_id)
    if not kelurahan_name:
        raise HTTPException(status_code=200, detail="Survey not found")

    survey = {}

    # Retrieve the latest survey for a kelurahan
    survey = crudsurvey.get_latest_survey_by_kelurahan_id(
        db, kelurahan_id=kelurahan_id)
    if not survey:
        return survey

    # Transform the survey to SurveyItem using Pydantic's from_orm method
    survey_item = upload_survey.SurveyItem.from_orm(survey).dict()

    # Prepare SurveyData and SurveyResponse
    survey_data = upload_survey.SurveyKelurahanLatest(
        kelurahan_id=kelurahan_id,
        kelurahan_name=kelurahan_name,
        surveys=survey_item,
    )

    return survey_item


@router.get("/all/latest", response_model=List[upload_survey.SurveyLatest])
def get_all_latest_surveys(db: Session = Depends(deps.get_db)):
    # Retrieve all latest surveys
    latest_surveys = []
    latest_surveys = crudsurvey.get_latest_surveys(db)

    if not latest_surveys:
        return latest_surveys

    return latest_surveys
