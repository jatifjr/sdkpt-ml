from typing import List
from sqlalchemy.orm import Session

from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate
from .base import CRUDBase


class CRUDSurvey(CRUDBase[Survey, SurveyCreate, SurveyUpdate]):
    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 10
    ) -> List[Survey]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create_bulk(
        self, db: Session, objs_in: List[SurveyCreate]
    ) -> List[Survey]:
        surveys = [self.model(**obj.dict()) for obj in objs_in]
        db.add_all(surveys)
        db.commit()
        return surveys


survey = CRUDSurvey(Survey)
