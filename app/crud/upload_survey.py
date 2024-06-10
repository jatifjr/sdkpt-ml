from typing import List, Optional, Dict
from calendar import month_name
from datetime import datetime
from sqlalchemy import func, extract
from sqlalchemy.orm import Session
import pandas as pd

from app.models.upload_survey import UploadSurvey
from app.schemas.upload_survey import SurveyBase, SurveyLatest, SurveyCreate, SurveyData, SurveyResponse, SurveyItem
from .base import CRUDBase


# ! DO NOT TOUCH THIS
class CRUDSurvey(CRUDBase[UploadSurvey, SurveyCreate, SurveyBase]):
    def get_by_kelurahan_id(
        self, db: Session, kelurahan_id: int, skip: int = 0, limit: int = 10
    ) -> List[UploadSurvey]:
        return db.query(self.model).filter_by(kelurahan_id=kelurahan_id).offset(skip).limit(limit).all()

    def get_kelurahan_name_by_id(
        self, db: Session, kelurahan_id: int
    ) -> str:
        survey = db.query(self.model).filter(
            self.model.kelurahan_id == kelurahan_id).first()
        if not survey:
            return None
        return survey.kelurahan

    # def read(self, db: Session, survey_id: int) -> Optional[Survey]:
    #     return db.query(self.model).filter(self.model.id == survey_id).first()

    def create_bulk(self, db: Session, objs_in: List[SurveyBase]) -> List[UploadSurvey]:
        surveys = []
        for obj_in in objs_in:
            survey = UploadSurvey(**obj_in.dict())
            db.add(survey)
            surveys.append(survey)
        db.commit()
        return surveys

    def create_from_excel(self, db: Session, file_path: str) -> List[UploadSurvey]:
        try:
            df = pd.read_excel(file_path)
            surveys = df.to_dict(orient="records")

            survey_objects = [SurveyBase(**survey) for survey in surveys]

            created_surveys = self.create_bulk(db, survey_objects)

            return created_surveys

        except Exception as e:
            db.rollback()
            raise e

    def get_latest_surveys(self, db: Session) -> List[SurveyLatest]:
        subquery = (
            db.query(
                self.model.kelurahan_id,
                func.row_number().over(
                    partition_by=self.model.kelurahan_id,
                    order_by=[self.model.created_at.desc()]
                ).label("row_number"),
                self.model.kelurahan,
                self.model.created_at
            )
            .subquery()
        )

        latest_surveys = (
            db.query(
                subquery.c.kelurahan_id,
                subquery.c.kelurahan,
                extract('month', subquery.c.created_at).label('bulan'),
                extract('year', subquery.c.created_at).label('tahun')
            )
            .filter(subquery.c.row_number == 1)
            .order_by(subquery.c.kelurahan_id.asc())
            .all()
        )

        survey_latest_list = []
        for survey in latest_surveys:
            bulan_name = month_name[int(survey.bulan)]
            survey_latest = SurveyLatest(
                kelurahan_id=survey.kelurahan_id,
                kelurahan_name=survey.kelurahan,
                bulan=bulan_name,
                tahun=survey.tahun
            )
            survey_latest_list.append(survey_latest)

        return survey_latest_list

    def get_latest_survey_by_kelurahan_id(self, db: Session, kelurahan_id: int) -> Optional[Dict]:
        latest_survey = db.query(self.model).filter(
            self.model.kelurahan_id == kelurahan_id).order_by(self.model.created_at.desc()).first()
        if not latest_survey:
            return None
        return SurveyItem.from_orm(latest_survey).dict()

    def transform_to_survey_item(self, surveys: List[UploadSurvey]) -> List[SurveyItem]:
        survey_items = []
        for survey in surveys:
            survey_item = SurveyItem(
                id=survey.id,
                created_at=survey.created_at,
                kelurahan_id=survey.kelurahan_id,
                kecamatan=survey.kecamatan,
                kelurahan=survey.kelurahan,
                kepadatan_penduduk=survey.kepadatan_penduduk,
                jumlah_penduduk=survey.jumlah_penduduk,
                jumlah_kasus_tb=survey.jumlah_kasus_tb,
                rasio_pasien_dan_jumlah_penduduk=survey.rasio_pasien_dan_jumlah_penduduk,
                jumlah_kasus_dm=survey.jumlah_kasus_dm,
                prevalensi_dm=survey.prevalensi_dm,
                jumlah_klinik_pratama=survey.jumlah_klinik_pratama,
                jumlah_klinik_utama=survey.jumlah_klinik_utama,
                rasio_penduduk_dan_fasyankes=survey.rasio_penduduk_dan_fasyankes,
                jumlah_puskemas=survey.jumlah_puskemas,
                pasien_jenis_kelamin_laki_laki=survey.pasien_jenis_kelamin_laki_laki,
                pasien_jenis_kelamin_perempuan=survey.pasien_jenis_kelamin_perempuan,
                pasien_pendidikan_terakhir_diploma=survey.pasien_pendidikan_terakhir_diploma,
                pasien_pendidikan_terakhir_s1=survey.pasien_pendidikan_terakhir_s1,
                pasien_pendidikan_terakhir_s2_s3=survey.pasien_pendidikan_terakhir_s2_s3,
                pasien_pendidikan_terakhir_tamat_sd=survey.pasien_pendidikan_terakhir_tamat_sd,
                pasien_pendidikan_terakhir_tamat_sma_sederajat=survey.pasien_pendidikan_terakhir_tamat_sma_sederajat,
                pasien_pendidikan_terakhir_tamat_smp_sederajat=survey.pasien_pendidikan_terakhir_tamat_smp_sederajat,
                pasien_pendidikan_terakhir_tidak_sekolah=survey.pasien_pendidikan_terakhir_tidak_sekolah,
                pasien_pendidikan_terakhir_tidak_tamat_sd=survey.pasien_pendidikan_terakhir_tidak_tamat_sd,
                pasien_status_bekerja_bekerja=survey.pasien_status_bekerja_bekerja,
                pasien_status_bekerja_tidak_bekerja=survey.pasien_status_bekerja_tidak_bekerja,
                pasien_status_bekerja_belum_bekerja=survey.pasien_status_bekerja_belum_bekerja,
                pasien_pendapatan_keluarga_kategori1=survey.pasien_pendapatan_keluarga_kategori1,
                pasien_pendapatan_keluarga_kategori2=survey.pasien_pendapatan_keluarga_kategori2,
                pasien_pendapatan_keluarga_kategori3=survey.pasien_pendapatan_keluarga_kategori3,
                pasien_pendapatan_keluarga_kategori4=survey.pasien_pendapatan_keluarga_kategori4,
                pasien_pendapatan_keluarga_kategori5=survey.pasien_pendapatan_keluarga_kategori5,
                pasien_efek_samping_obat_tidak=survey.pasien_efek_samping_obat_tidak,
                pasien_efek_samping_obat_ya=survey.pasien_efek_samping_obat_ya,
                pasien_pengaruh_pendapatan_tidak=survey.pasien_pengaruh_pendapatan_tidak,
                pasien_pengaruh_pendapatan_ya=survey.pasien_pengaruh_pendapatan_ya,
                pasien_kategori_bmi_berat_badan_kurang=survey.pasien_kategori_bmi_berat_badan_kurang,
                pasien_kategori_bmi_berat_badan_normal=survey.pasien_kategori_bmi_berat_badan_normal,
                pasien_kategori_bmi_kelebihan_berat_badan=survey.pasien_kategori_bmi_kelebihan_berat_badan,
                pasien_kategori_bmi_obesitas_i=survey.pasien_kategori_bmi_obesitas_i,
                pasien_kategori_bmi_obesitas_ii=survey.pasien_kategori_bmi_obesitas_ii,
                pasien_kategori_usia_anak_anak=survey.pasien_kategori_usia_anak_anak,
                pasien_kategori_usia_balita=survey.pasien_kategori_usia_balita,
                pasien_kategori_usia_dewasa_akhir=survey.pasien_kategori_usia_dewasa_akhir,
                pasien_kategori_usia_dewasa_awal=survey.pasien_kategori_usia_dewasa_awal,
                pasien_kategori_usia_lansia_akhir=survey.pasien_kategori_usia_lansia_akhir,
                pasien_kategori_usia_lansia_awal=survey.pasien_kategori_usia_lansia_awal,
                pasien_kategori_usia_manula=survey.pasien_kategori_usia_manula,
                pasien_kategori_usia_remaja_akhir=survey.pasien_kategori_usia_remaja_akhir,
                pasien_kategori_usia_remaja_awal=survey.pasien_kategori_usia_remaja_awal,
                pasien_kategori_pengetahuan_baik=survey.pasien_kategori_pengetahuan_baik,
                pasien_kategori_pengetahuan_buruk=survey.pasien_kategori_pengetahuan_buruk,
                pasien_kategori_pengetahuan_cukup=survey.pasien_kategori_pengetahuan_cukup,
                pasien_kategori_pengetahuan_kurang=survey.pasien_kategori_pengetahuan_kurang,
                pasien_kategori_perilaku_baik=survey.pasien_kategori_perilaku_baik,
                pasien_kategori_perilaku_cukup=survey.pasien_kategori_perilaku_cukup,
                pasien_kategori_perilaku_kurang=survey.pasien_kategori_perilaku_kurang,
                pasien_kategori_perilaku_sangat_kurang=survey.pasien_kategori_perilaku_sangat_kurang,
                pasien_kategori_literasi_excellent=survey.pasien_kategori_literasi_excellent,
                pasien_kategori_literasi_inadequate=survey.pasien_kategori_literasi_inadequate,
                pasien_kategori_literasi_problematic=survey.pasien_kategori_literasi_problematic,
                pasien_kategori_literasi_sufficient=survey.pasien_kategori_literasi_sufficient,
                pasien_kategori_stigma_tidak_stigma=survey.pasien_kategori_stigma_tidak_stigma,
                pasien_kategori_stigma_stigma_rendah=survey.pasien_kategori_stigma_stigma_rendah,
                pasien_kategori_stigma_stigma_sangat_rendah=survey.pasien_kategori_stigma_stigma_sangat_rendah,
                pasien_kategori_stigma_stigma_sedang=survey.pasien_kategori_stigma_stigma_sedang,
                pasien_kategori_stigma_stigma_tinggi=survey.pasien_kategori_stigma_stigma_tinggi,
                keluarga_pendidikan_terakhir_diploma=survey.keluarga_pendidikan_terakhir_diploma,
                keluarga_pendidikan_terakhir_s1=survey.keluarga_pendidikan_terakhir_s1,
                keluarga_pendidikan_terakhir_s2_s3=survey.keluarga_pendidikan_terakhir_s2_s3,
                keluarga_pendidikan_terakhir_tamat_sd=survey.keluarga_pendidikan_terakhir_tamat_sd,
                keluarga_pendidikan_terakhir_tamat_sma_sederajat=survey.keluarga_pendidikan_terakhir_tamat_sma_sederajat,
                keluarga_pendidikan_terakhir_tamat_smp_sederajat=survey.keluarga_pendidikan_terakhir_tamat_smp_sederajat,
                keluarga_pendidikan_terakhir_tidak_sekolah=survey.keluarga_pendidikan_terakhir_tidak_sekolah,
                keluarga_pendidikan_terakhir_tidak_tamat_sd=survey.keluarga_pendidikan_terakhir_tidak_tamat_sd,
                keluarga_status_bekerja_bekerja=survey.keluarga_status_bekerja_bekerja,
                keluarga_status_bekerja_tidak_bekerja=survey.keluarga_status_bekerja_tidak_bekerja,
                keluarga_riwayat_tb_di_rumah_ada=survey.keluarga_riwayat_tb_di_rumah_ada,
                keluarga_riwayat_tb_di_rumah_tidak_ada=survey.keluarga_riwayat_tb_di_rumah_tidak_ada,
                keluarga_tpt_serumah_ada=survey.keluarga_tpt_serumah_ada,
                keluarga_tpt_serumah_tidak_ada=survey.keluarga_tpt_serumah_tidak_ada,
                keluarga_jenis_lantai_kayu=survey.keluarga_jenis_lantai_kayu,
                keluarga_jenis_lantai_tanah=survey.keluarga_jenis_lantai_tanah,
                keluarga_jenis_lantai_ubin_keramik_tegel=survey.keluarga_jenis_lantai_ubin_keramik_tegel,
                keluarga_cahaya_matahari_masuk_tidak=survey.keluarga_cahaya_matahari_masuk_tidak,
                keluarga_cahaya_matahari_masuk_ya=survey.keluarga_cahaya_matahari_masuk_ya,
                keluarga_kategori_pengetahuan_baik=survey.keluarga_kategori_pengetahuan_baik,
                keluarga_kategori_pengetahuan_buruk=survey.keluarga_kategori_pengetahuan_buruk,
                keluarga_kategori_pengetahuan_cukup=survey.keluarga_kategori_pengetahuan_cukup,
                keluarga_kategori_pengetahuan_kurang=survey.keluarga_kategori_pengetahuan_kurang,
                keluarga_kategori_literasi_inadequate=survey.keluarga_kategori_literasi_inadequate,
                keluarga_kategori_literasi_problematic=survey.keluarga_kategori_literasi_problematic,
                keluarga_kategori_literasi_sufficient=survey.keluarga_kategori_literasi_sufficient,
                keluarga_kategori_literasi_excellent=survey.keluarga_kategori_literasi_excellent,
                keluarga_kategori_stigma_stigma_rendah=survey.keluarga_kategori_stigma_stigma_rendah,
                keluarga_kategori_stigma_stigma_sangat_rendah=survey.keluarga_kategori_stigma_stigma_sangat_rendah,
                keluarga_kategori_stigma_stigma_sedang=survey.keluarga_kategori_stigma_stigma_sedang,
                keluarga_kategori_stigma_stigma_tinggi=survey.keluarga_kategori_stigma_stigma_tinggi,
                keluarga_kategori_stigma_tidak_stigma=survey.keluarga_kategori_stigma_tidak_stigma,
                keluarga_kategori_perilaku_baik=survey.keluarga_kategori_perilaku_baik,
                keluarga_kategori_perilaku_cukup=survey.keluarga_kategori_perilaku_cukup,
                keluarga_kategori_perilaku_kurang=survey.keluarga_kategori_perilaku_kurang,
                keluarga_kategori_perilaku_sangat_kurang=survey.keluarga_kategori_perilaku_sangat_kurang,
                masyarakat_pendidikan_terakhir_diploma=survey.masyarakat_pendidikan_terakhir_diploma,
                masyarakat_pendidikan_terakhir_s1=survey.masyarakat_pendidikan_terakhir_s1,
                masyarakat_pendidikan_terakhir_s2_s3=survey.masyarakat_pendidikan_terakhir_s2_s3,
                masyarakat_pendidikan_terakhir_tamat_sd=survey.masyarakat_pendidikan_terakhir_tamat_sd,
                masyarakat_pendidikan_terakhir_tamat_sma_sederajat=survey.masyarakat_pendidikan_terakhir_tamat_sma_sederajat,
                masyarakat_pendidikan_terakhir_tamat_smp_sederajat=survey.masyarakat_pendidikan_terakhir_tamat_smp_sederajat,
                masyarakat_pendidikan_terakhir_tidak_sekolah=survey.masyarakat_pendidikan_terakhir_tidak_sekolah,
                masyarakat_pendidikan_terakhir_tidak_tamat_sd=survey.masyarakat_pendidikan_terakhir_tidak_tamat_sd,
                masyarakat_status_perkajaan_bekerja=survey.masyarakat_status_perkajaan_bekerja,
                masyarakat_status_perkajaan_tidak_bekerja=survey.masyarakat_status_perkajaan_tidak_bekerja,
                masyarakat_kategori_pendapatan_kategori1=survey.masyarakat_kategori_pendapatan_kategori1,
                masyarakat_kategori_pendapatan_kategori2=survey.masyarakat_kategori_pendapatan_kategori2,
                masyarakat_kategori_pendapatan_kategori3=survey.masyarakat_kategori_pendapatan_kategori3,
                masyarakat_kategori_pendapatan_kategori4=survey.masyarakat_kategori_pendapatan_kategori4,
                masyarakat_kategori_pendapatan_kategori5=survey.masyarakat_kategori_pendapatan_kategori5,
                masyarakat_riwayat_tb_keluarga_ada=survey.masyarakat_riwayat_tb_keluarga_ada,
                masyarakat_riwayat_tb_keluarga_tidak_ada=survey.masyarakat_riwayat_tb_keluarga_tidak_ada,
                masyarakat_kategori_bmi_berat_badan_kurang=survey.masyarakat_kategori_bmi_berat_badan_kurang,
                masyarakat_kategori_bmi_berat_badan_normal=survey.masyarakat_kategori_bmi_berat_badan_normal,
                masyarakat_kategori_bmi_kelebihan_berat_badan=survey.masyarakat_kategori_bmi_kelebihan_berat_badan,
                masyarakat_kategori_bmi_obesitas_i=survey.masyarakat_kategori_bmi_obesitas_i,
                masyarakat_kategori_bmi_obesitas_ii=survey.masyarakat_kategori_bmi_obesitas_ii,
                masyarakat_kategori_pengetahuan_baik=survey.masyarakat_kategori_pengetahuan_baik,
                masyarakat_kategori_pengetahuan_buruk=survey.masyarakat_kategori_pengetahuan_buruk,
                masyarakat_kategori_pengetahuan_cukup=survey.masyarakat_kategori_pengetahuan_cukup,
                masyarakat_kategori_pengetahuan_kurang=survey.masyarakat_kategori_pengetahuan_kurang,
                masyarakat_kategori_perilaku_baik=survey.masyarakat_kategori_perilaku_baik,
                masyarakat_kategori_perilaku_cukup=survey.masyarakat_kategori_perilaku_cukup,
                masyarakat_kategori_perilaku_kurang=survey.masyarakat_kategori_perilaku_kurang,
                masyarakat_kategori_perilaku_sangat_kurang=survey.masyarakat_kategori_perilaku_sangat_kurang,
                masyarakat_kategori_literasi_excellent=survey.masyarakat_kategori_literasi_excellent,
                masyarakat_kategori_literasi_inadequate=survey.masyarakat_kategori_literasi_inadequate,
                masyarakat_kategori_literasi_problematic=survey.masyarakat_kategori_literasi_problematic,
                masyarakat_kategori_literasi_sufficient=survey.masyarakat_kategori_literasi_sufficient,
                masyarakat_kategori_stigma_stigma_rendah=survey.masyarakat_kategori_stigma_stigma_rendah,
                masyarakat_kategori_stigma_stigma_sangat_rendah=survey.masyarakat_kategori_stigma_stigma_sangat_rendah,
                masyarakat_kategori_stigma_stigma_sedang=survey.masyarakat_kategori_stigma_stigma_sedang,
                masyarakat_kategori_stigma_stigma_tinggi=survey.masyarakat_kategori_stigma_stigma_tinggi,
                masyarakat_kategori_stigma_tidak_stigma=survey.masyarakat_kategori_stigma_tidak_stigma,
            )
            survey_items.append(survey_item)
        return survey_items


upload_survey = CRUDSurvey(UploadSurvey)
