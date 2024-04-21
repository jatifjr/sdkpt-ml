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


survey = CRUDSurvey(Survey)
