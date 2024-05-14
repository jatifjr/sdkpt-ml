from typing import Any, Dict, List, Union, Optional, Type

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.models.patient import Patient
from app.models.kelurahan import Kelurahan
from app.schemas.patient import PatientCreate, PatientResponse
from app.crud.base import CRUDBase


class CRUDPatient(CRUDBase[Patient, PatientCreate, PatientResponse]):
    def __init__(self, model: Type[Patient] = Patient):
        super().__init__(model)

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int, skip: int = 0, limit: int = 10) -> List[Patient]:
        # Fetch the kelurahan with the given id
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            return []

        # Get the kode_kd from the kelurahan
        kode_kd = kelurahan.kode_kd

        # Fetch patients with matching kelurahan_domisili with pagination
        patients = db.query(Patient).filter(
            Patient.kelurahan_domisili == kode_kd).offset(skip).limit(limit).all()
        return patients


patient = CRUDPatient(Patient)
