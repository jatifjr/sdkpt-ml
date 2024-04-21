from typing import Optional

from sqlalchemy.orm import Session

from app.models.intervention import Intervention
from app.schemas.intervention import InterventionCreate, InterventionUpdate
from .base import CRUDBase


class CRUDIntervention(CRUDBase[Intervention, InterventionCreate, InterventionUpdate]):
    def get_by_id(self, db: Session, intervention_id: int) -> Optional[Intervention]:
        return self.get(db, id=intervention_id)


intervention = CRUDIntervention(Intervention)
