from typing import Type, Optional
from sqlalchemy.orm import Session
from app.models.kelurahan import Kelurahan as KelurahanModel
from app.schemas.kelurahan import Kelurahan as KelurahanSchema
from app.crud.base import CRUDBase


class CRUDKelurahan(CRUDBase[KelurahanModel, KelurahanSchema, KelurahanSchema]):
    def __init__(self, model: Type[KelurahanModel] = KelurahanModel):
        super().__init__(model)

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int) -> Optional[KelurahanSchema]:
        kelurahan = db.query(KelurahanModel).filter(
            KelurahanModel.id == kelurahan_id).first()
        return kelurahan


kelurahan = CRUDKelurahan(KelurahanModel)
