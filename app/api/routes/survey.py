from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import upload_survey as crudsurvey
from app.schemas import upload_survey


router = APIRouter()


@router.get("/kelurahan", response_model=upload_survey.SurveyResponse)
def read_surveys(
    kelurahan_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(deps.get_db),
):
    # Retrieve kelurahan name
    kelurahan_name = crudsurvey.get_kelurahan_name_by_id(db, kelurahan_id)
    if not kelurahan_name:
        raise HTTPException(status_code=404, detail="Kelurahan not found")

    # Retrieve surveys for a kelurahan
    surveys = crudsurvey.get_by_kelurahan_id(
        db, kelurahan_id=kelurahan_id, skip=skip, limit=limit
    )

    # Check if surveys are empty
    if not surveys:
        raise HTTPException(status_code=404, detail="Surveys not found")

    # Sort surveys by created_at
    surveys.sort(key=lambda x: (x.created_at.year, x.created_at.month))

    # Transform surveys to SurveyItem using the CRUD method
    survey_items = crudsurvey.transform_to_survey_item(surveys)

    # Prepare SurveyData and SurveyResponse
    survey_data = upload_survey.SurveyData(
        kelurahan_id=kelurahan_id,
        kelurahan_name=kelurahan_name,
        surveys=survey_items,
    )

    response = upload_survey.SurveyResponse(
        status="OK", message="Success", data=survey_data
    )

    return response


@router.get("/kelurahan/latest", response_model=upload_survey.SurveyItem)
def get_latest_kelurahan(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db),
):
    # Retrieve kelurahan name
    kelurahan_name = crudsurvey.get_kelurahan_name_by_id(db, kelurahan_id)
    if not kelurahan_name:
        raise HTTPException(status_code=404, detail="Kelurahan not found")

    # Retrieve the latest survey for a kelurahan
    survey = crudsurvey.get_latest_survey_by_kelurahan_id(
        db, kelurahan_id=kelurahan_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Surveys not found")

    # Transform the survey to SurveyItem using Pydantic's from_orm method
    survey_item = upload_survey.SurveyItem.from_orm(survey).dict()
    print(survey_item)

    # Prepare SurveyData and SurveyResponse
    survey_data = upload_survey.SurveyKelurahanLatest(
        kelurahan_id=kelurahan_id,
        kelurahan_name=kelurahan_name,
        surveys=survey_item,
    )

    return survey_item


@router.get("/all/latest", response_model=List[upload_survey.SurveyLatest])
def get_all_latest_surveys(db: Session = Depends(deps.get_db)):
    try:
        # Retrieve all latest surveys
        latest_surveys = crudsurvey.get_latest_surveys(db)

        if not latest_surveys:
            raise HTTPException(status_code=404, detail="No surveys found")

        return latest_surveys

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/kelurahan", response_model=survey_schemas.SurveyResponse)
# def read_surveys(
#     kelurahan_id: int,
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 10
# ):
#     surveys = survey_crud.get_by_kelurahan_id(
#         db, kelurahan_id=kelurahan_id, skip=skip, limit=limit)

#     if not surveys:
#         raise HTTPException(status_code=404, detail="No surveys found")

#     kelurahan_name = survey_crud.get_kelurahan_name_by_id(db, kelurahan_id)

#     surveys.sort(key=lambda x: (x.tahun, x.bulan))

#     survey_items = survey_crud.transform_to_survey_items(surveys)

#     survey_data = survey_schemas.SurveyData(
#         kelurahan_id=kelurahan_id,
#         kelurahan_name=kelurahan_name,
#         surveys=survey_items
#     )

#     response = survey_schemas.SurveyResponse(
#         status="OK",
#         message="Success",
#         data=survey_data
#     )

#     return response


# @router.post("/", response_model=survey_schemas.Survey)
# def create_survey(
#     survey_in: survey_schemas.SurveyCreate,
#     db: Session = Depends(deps.get_db)
# ):
#     return survey_crud.create(db=db, obj_in=survey_in)


# @router.post("/bulk", response_model=List[survey_schemas.Survey])
# def create_bulk_surveys(
#     surveys_in: List[survey_schemas.SurveyCreate],
#     db: Session = Depends(deps.get_db)
# ):
#     return survey_crud.create_bulk(db=db, objs_in=surveys_in)


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
