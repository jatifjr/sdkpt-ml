from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import survey as survey_crud
from app.schemas import survey as survey_schemas

router = APIRouter()


# @router.get("/{survey_id}", response_model=survey_schemas.Survey)
# def read_survey_by_id(
#     survey_id: int,
#     db: Session = Depends(deps.get_db)
# ):
#     survey = survey_crud.get(db, id=survey_id)
#     if not survey:
#         raise HTTPException(status_code=404, detail="Survey not found")
#     return survey


@router.get("/", response_model=List[survey_schemas.Survey])
def read_surveys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10
):
    surveys = survey_crud.get_multi(db, skip=skip, limit=limit)
    if not surveys:
        raise HTTPException(status_code=404, detail="No surveys found")
    return surveys


@router.post("/", response_model=survey_schemas.Survey)
def create_survey(
    survey_in: survey_schemas.SurveyCreate,
    db: Session = Depends(deps.get_db)
):
    return survey_crud.create(db=db, obj_in=survey_in)


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
