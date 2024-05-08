from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import survey as survey_crud
from app.schemas import survey as survey_schemas

router = APIRouter()


@router.get("/{kelurahan_id}", response_model=survey_schemas.SurveyResponse)
def read_surveys(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10
):
    surveys = survey_crud.get_by_kelurahan_id(
        db, kelurahan_id=kelurahan_id, skip=skip, limit=limit)

    if not surveys:
        raise HTTPException(status_code=404, detail="No surveys found")

    kelurahan_name = survey_crud.get_kelurahan_name_by_id(db, kelurahan_id)

    surveys.sort(key=lambda x: (x.tahun, x.bulan))

    survey_items = survey_crud.transform_to_survey_items(surveys)

    survey_data = survey_schemas.SurveyData(
        kelurahan_id=kelurahan_id,
        kelurahan_name=kelurahan_name,
        surveys=survey_items
    )

    response = survey_schemas.SurveyResponse(
        status="OK",
        message="Success",
        data=survey_data
    )

    return response


@router.get("/latest", response_model=List[survey_schemas.SurveyLatest])
def get_all_latest_surveys(
    db: Session = Depends(deps.get_db)
):
    latest_surveys = survey_crud.get_latest_surveys(db)

    if not latest_surveys:
        raise HTTPException(status_code=404, detail="No surveys found")

    return latest_surveys


@router.post("/", response_model=survey_schemas.Survey)
def create_survey(
    survey_in: survey_schemas.SurveyCreate,
    db: Session = Depends(deps.get_db)
):
    return survey_crud.create(db=db, obj_in=survey_in)


@router.post("/bulk", response_model=List[survey_schemas.Survey])
def create_bulk_surveys(
    surveys_in: List[survey_schemas.SurveyCreate],
    db: Session = Depends(deps.get_db)
):
    return survey_crud.create_bulk(db=db, objs_in=surveys_in)


# @router.put("/{survey_id}", response_model=survey_schemas.Survey)
# def update_survey(
#     survey_id: int,
#     survey_in: survey_schemas.SurveyUpdate,
#     db: Session = Depends(deps.get_db)
# ):
#     survey = survey_crud.get(db, id=survey_id)
#     if not survey:
#         raise HTTPException(status_code=404, detail="Survey not found")
#     return survey_crud.update(db=db, db_obj=survey, obj_in=survey_in)


# @router.delete("/{survey_id}", response_model=dict)
# def delete_survey(
#     survey_id: int,
#     db: Session = Depends(deps.get_db)
# ):
#     survey = survey_crud.get(db, id=survey_id)
#     if not survey:
#         raise HTTPException(status_code=404, detail="Survey not found")
#     survey_crud.remove(db=db, id=survey_id)
#     return {"message": "Survey deleted"}
