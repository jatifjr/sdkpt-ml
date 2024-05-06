from typing import List
from sqlalchemy.orm import Session
from calendar import month_name

from app.models.survey import Survey
from app.schemas.survey import SurveyCreate, SurveyUpdate, SurveyItem
from .base import CRUDBase


class CRUDSurvey(CRUDBase[Survey, SurveyCreate, SurveyUpdate]):
    def get_by_kelurahan_id(
        self, db: Session, kelurahan_id: int, skip: int = 0, limit: int = 10
    ) -> List[Survey]:
        return db.query(self.model).filter_by(kelurahan_id=kelurahan_id).offset(skip).limit(limit).all()

    def get_kelurahan_name_by_id(
        self, db: Session, kelurahan_id: int
    ) -> str:
        survey = db.query(self.model).filter(
            self.model.kelurahan_id == kelurahan_id).first()
        if not survey:
            return None
        return survey.kelurahan_name

    def create_bulk(
        self, db: Session, objs_in: List[SurveyCreate]
    ) -> List[Survey]:
        surveys = [self.model(**obj.dict()) for obj in objs_in]
        db.add_all(surveys)
        db.commit()
        return surveys

    def transform_to_survey_items(
        self, surveys: List[Survey]
    ) -> List[SurveyItem]:
        survey_items = []
        for survey in surveys:
            survey_item = SurveyItem(
                id=survey.id,
                created_at=survey.created_at,
                tahun=survey.tahun,
                bulan=month_name[survey.bulan],
                population_density=survey.population_density,
                population=survey.population,
                tb_cases=survey.tb_cases,
                population_tb_cases_ratio=survey.population_tb_cases_ratio,
                dm_cases=survey.dm_cases,
                jumlah_klinik_pratama=survey.jumlah_klinik_pratama,
                jumlah_klinik_utama=survey.jumlah_klinik_utama,
                gender_perempuan=survey.gender_perempuan,
                gender_laki_laki=survey.gender_laki_laki,
                usia_paruh_baya=survey.usia_paruh_baya,
                usia_pensiun=survey.usia_pensiun,
                usia_pekerja_awal=survey.usia_pekerja_awal,
                usia_lanjut=survey.usia_lanjut,
                usia_muda=survey.usia_muda,
                usia_pra_pensiun=survey.usia_pra_pensiun,
                usia_anak=survey.usia_anak,
                pendidikan_diploma=survey.pendidikan_diploma,
                pendidikan_s1=survey.pendidikan_s1,
                pendidikan_s2_s3=survey.pendidikan_s2_s3,
                pendidikan_tamat_sd=survey.pendidikan_tamat_sd,
                pendidikan_tamat_sma=survey.pendidikan_tamat_sma,
                pendidikan_tamat_smp=survey.pendidikan_tamat_smp,
                pendidikan_tidak_sekolah=survey.pendidikan_tidak_sekolah,
                pendidikan_tidak_tamat_sd=survey.pendidikan_tidak_tamat_sd,
                status_bekerja_tidak_bekerja=survey.status_bekerja_tidak_bekerja,
                status_bekerja_bekerja=survey.status_bekerja_bekerja,
                pendapatan_keluarga_kategori_1=survey.pendapatan_keluarga_kategori_1,
                pendapatan_keluarga_kategori_2=survey.pendapatan_keluarga_kategori_2,
                pendapatan_keluarga_kategori_3=survey.pendapatan_keluarga_kategori_3,
                pendapatan_keluarga_kategori_4=survey.pendapatan_keluarga_kategori_4,
                pendapatan_keluarga_kategori_5=survey.pendapatan_keluarga_kategori_5,
                tpt_serumah_tidak_mendapatkan_tpt=survey.tpt_serumah_tidak_mendapatkan_tpt,
                tpt_serumah_tidak_ada=survey.tpt_serumah_tidak_ada,
                tpt_serumah_ada=survey.tpt_serumah_ada,
                perokok_aktif_tidak=survey.perokok_aktif_tidak,
                perokok_aktif_ya=survey.perokok_aktif_ya,
                konsumsi_alkohol_tidak=survey.konsumsi_alkohol_tidak,
                konsumsi_alkohol_ya=survey.konsumsi_alkohol_ya,
                kategori_pengetahuan_cukup=survey.kategori_pengetahuan_cukup,
                kategori_pengetahuan_kurang=survey.kategori_pengetahuan_kurang,
                kategori_pengetahuan_baik=survey.kategori_pengetahuan_baik,
                kategori_pengetahuan_buruk=survey.kategori_pengetahuan_buruk,
                kategori_literasi_problematic=survey.kategori_literasi_problematic,
                kategori_literasi_excellent=survey.kategori_literasi_excellent,
                kategori_literasi_inadequate=survey.kategori_literasi_inadequate,
                kategori_literasi_sufficient=survey.kategori_literasi_sufficient,
                kategori_stigma_tinggi=survey.kategori_stigma_tinggi,
                kategori_stigma_sedang=survey.kategori_stigma_sedang,
                kategori_stigma_rendah=survey.kategori_stigma_rendah,
                kategori_stigma_tidak=survey.kategori_stigma_tidak
            )
            survey_items.append(survey_item)
        return survey_items


survey = CRUDSurvey(Survey)
