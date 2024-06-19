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
        outcome_counts = self.get_patient_count_by_treatment_outcome(
            db, kelurahan_id)

        # Calculate jumlah_kasus as the sum of the outcomes
        jumlah_kasus = outcome_counts.sembuh + \
            outcome_counts.gagal + outcome_counts.meninggal

        return PatientCaseAndOutcomeCounts(jumlah_kasus=jumlah_kasus, sembuh=outcome_counts.sembuh, gagal=outcome_counts.gagal, meninggal=outcome_counts.meninggal)

    def get_case_count_by_kelurahan_id(self, db: Session, kelurahan_id: int) -> int:
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            return 0

        one_year_ago = datetime.now() - timedelta(days=365)

        case_count = db.query(func.count()).filter(
            Patient.kelurahan_domisili == kelurahan.kode_kd,
            Patient.tahun == one_year_ago.year
        ).scalar()
        return case_count

    def get_patient_count_by_treatment_outcome(self, db: Session, kelurahan_id: int) -> PatientOutcomeCounts:
        one_year_ago = datetime.now() - timedelta(days=365)
        kelurahan = db.query(Kelurahan).filter(
            Kelurahan.id == kelurahan_id).first()
        if not kelurahan:
            raise HTTPException(status_code=404, detail="Kelurahan not found")

        kode_kd = kelurahan.kode_kd

        # Calculate the outcome counts
        outcome_counts = db.query(
            func.sum(case((Patient.pengobatan_terakhir.ilike(
                'sembuh'), 1), else_=0)).label('sembuh'),
            func.sum(case((Patient.pengobatan_terakhir.ilike(
                'putus berobat'), 1), else_=0)).label('gagal'),
            func.sum(case((Patient.pengobatan_terakhir.ilike(
                'meninggal'), 1), else_=0)).label('meninggal'),
            func.sum(case((Patient.pengobatan_terakhir.ilike(
                'pengobatan lengkap'), 1), else_=0)).label('pengobatan_lengkap')
        ).filter(
            Patient.kelurahan_domisili == kode_kd,
            Patient.tahun == one_year_ago.year,
        ).first()

        # Combine 'pengobatan_lengkap' with 'sembuh'
        outcome_counts_dict = {
            'sembuh': outcome_counts.sembuh + outcome_counts.pengobatan_lengkap,
            'gagal': outcome_counts.gagal,
            'meninggal': outcome_counts.meninggal
        }

        return PatientOutcomeCounts(**outcome_counts_dict)

    def get_total_cases_and_outcomes(self, db: Session) -> TotalCasesAndOutcomesResponse:
        one_year_ago = datetime.now() - timedelta(days=365)

        # Count total cases with specified outcomes
        case_count = db.query(func.count()).filter(
            Patient.tahun == one_year_ago.year,
            func.lower(Patient.pengobatan_terakhir).in_(
                ['sembuh', 'putus berobat', 'meninggal', 'pengobatan lengkap']
            )
        ).scalar()

        # Count outcomes
        outcome_counts = db.query(
            func.count(case((Patient.pengobatan_terakhir.ilike('sembuh'), 1))),
            func.count(
                case((Patient.pengobatan_terakhir.ilike('putus berobat'), 1))),
            func.count(
                case((Patient.pengobatan_terakhir.ilike('meninggal'), 1)))
        ).filter(
            Patient.tahun == one_year_ago.year
        ).first()

        # Count new cases in the last 6 months
        six_months_ago = datetime.now() - timedelta(days=180)
        new_cases = db.query(
            func.count()
        ).filter(
            Patient.pengobatan_terakhir.ilike('pengobatan lengkap'),
            Patient.tahun == one_year_ago.year,
            Patient.bulan >= six_months_ago.month
        ).scalar()

        return TotalCasesAndOutcomesResponse(
            kasus_aktif=case_count,
            kasus_baru=new_cases,
            sembuh=outcome_counts[0],
            gagal=outcome_counts[1],
            meninggal=outcome_counts[2]
        )


patient = CRUDPatient(Patient)
