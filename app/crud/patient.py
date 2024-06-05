from typing import Type
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from fastapi import HTTPException

from app.crud.base import CRUDBase
from app.models.patient import Patient
from app.models.kelurahan import Kelurahan
from app.schemas.patient import PatientCreate, PatientResponse, PatientCaseAndOutcomeCounts, PatientOutcomeCounts, TotalCasesAndOutcomesResponse


class CRUDPatient(CRUDBase[Patient, PatientCreate, PatientResponse]):
    def __init__(self, model: Type[Patient] = Patient):
        super().__init__(model)

    def get_by_kelurahan_id(self, db: Session, kelurahan_id: int, skip: int = 0, limit: int = 10):
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            return []

        kode_kd = kelurahan.kode_kd

        patients = db.query(Patient).filter(
            Patient.kelurahan_domisili == kode_kd).offset(skip).limit(limit).all()
        return patients

    def get_case_and_outcome_counts(self, db: Session, kelurahan_id: int) -> PatientCaseAndOutcomeCounts:
        case_count = self.get_case_count_by_kelurahan_id(db, kelurahan_id)
        outcome_counts = self.get_patient_count_by_treatment_outcome(
            db, kelurahan_id)
        return PatientCaseAndOutcomeCounts(jumlah_kasus=case_count, sembuh=outcome_counts.sembuh, gagal=outcome_counts.gagal, meninggal=outcome_counts.meninggal)

    def get_case_count_by_kelurahan_id(self, db: Session, kelurahan_id: int) -> int:
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            return 0

        one_year_ago = datetime.now() - timedelta(days=365)

        case_count = db.query(func.count()).filter(
            Patient.kelurahan_domisili == kelurahan.kode_kd,
            Patient.tahun >= one_year_ago.year
        ).scalar()
        return case_count

    def get_patient_count_by_treatment_outcome(self, db: Session, kelurahan_id: int) -> PatientOutcomeCounts:
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            raise HTTPException(status_code=404, detail="Kelurahan not found")

        kode_kd = kelurahan.kode_kd

        result = db.query(
            Patient.pengobatan_terakhir,
            func.count(Patient.pengobatan_terakhir).label("count")
        ).filter(
            Patient.kelurahan_domisili == kode_kd,
            func.lower(Patient.pengobatan_terakhir).in_(
                ['sembuh', 'putus berobat', 'meninggal'])
        ).group_by(
            Patient.pengobatan_terakhir
        ).all()

        outcome_counts = {'sembuh': 0, 'gagal': 0, 'meninggal': 0}
        for row in result:
            outcome = row.pengobatan_terakhir.lower().replace(" ", "_")
            outcome_counts[outcome] = row.count

        return PatientOutcomeCounts(**outcome_counts)

    def get_total_cases_and_outcomes(self, db: Session) -> TotalCasesAndOutcomesResponse:
        one_year_ago = datetime.now() - timedelta(days=365)

        # Count total cases until one year ago
        case_count = db.query(func.count()).filter(
            Patient.tahun >= one_year_ago.year
        ).scalar()

        # Count outcomes
        outcome_counts = db.query(
            func.count(case((Patient.pengobatan_terakhir.ilike('Sembuh'), 1))),
            func.count(
                case((Patient.pengobatan_terakhir.ilike('Putus Berobat'), 1))),
            func.count(
                case((Patient.pengobatan_terakhir.ilike('Meninggal'), 1)))
        ).first()

        return TotalCasesAndOutcomesResponse(
            jumlah_kasus=case_count,
            sembuh=outcome_counts[0],
            gagal=outcome_counts[1],
            meninggal=outcome_counts[2]
        )


patient = CRUDPatient(Patient)
