from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import upload_survey as crudsurvey
from app.crud import kelurahan as crudkelurahan
from app.schemas import upload_survey


router = APIRouter()


# ! DO NOT TOUCH THIS
@router.get("/kelurahan/latest", response_model=Dict)
def get_latest_kelurahan(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db),
):
    # Retrieve kelurahan name
    kelurahan_name = crudsurvey.get_kelurahan_name_by_id(db, kelurahan_id)
    if not kelurahan_name:
        raise HTTPException(status_code=200, detail="Survey not found")

    # Retrieve the latest survey for a kelurahan
    survey = crudsurvey.get_latest_survey_by_kelurahan_id(
        db, kelurahan_id=kelurahan_id)
    if not survey:
        raise HTTPException(status_code=200, detail="Survey not found")

    # Retrieve merged category sums
    merged_sums = crudsurvey.get_merged_category_sums(db)
    merged_sums_for_kelurahan = next(
        (item for item in merged_sums if item["kelurahan_id"] == kelurahan_id), None)

    if not merged_sums_for_kelurahan:
        raise HTTPException(status_code=200, detail="Survey not found")

    # Remove 'kelurahan_id' from merged_sums_for_kelurahan
    stats = {k: v for k, v in merged_sums_for_kelurahan.items() if k !=
             "kelurahan_id"}

    # Prepare the response
    response = {
        "kelurahan_id": kelurahan_id,
        "kelurahan_name": kelurahan_name,
        "stats": stats
    }

    return stats


@router.get("/all/latest", response_model=List[upload_survey.SurveyLatest])
def get_all_latest_surveys(db: Session = Depends(deps.get_db)):
    # Retrieve all latest surveys
    latest_surveys = []
    latest_surveys = crudsurvey.get_latest_surveys(db)

    if not latest_surveys:
        return latest_surveys

    return latest_surveys
