from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class SurveyBase(BaseModel):
    kelurahan_id: int
    kelurahan_name: str
    population_density: Optional[int] = None
    population: Optional[int] = None
    tb_cases: Optional[int] = None
    population_tb_cases_ratio: Optional[float] = None
    dm_cases: Optional[int] = None
    jumlah_klinik_pratama: Optional[int] = None
    jumlah_klinik_utama: Optional[int] = None
    gender_perempuan: Optional[int] = None
    gender_laki_laki: Optional[int] = None
    usia_paruh_baya: Optional[int] = None
    usia_pensiun: Optional[int] = None
    usia_pekerja_awal: Optional[int] = None
    usia_lanjut: Optional[int] = None
    usia_muda: Optional[int] = None
    usia_pra_pensiun: Optional[int] = None
    usia_anak: Optional[int] = None
    pendidikan_diploma: Optional[int] = None
    pendidikan_s1: Optional[int] = None
    pendidikan_s2_s3: Optional[int] = None
    pendidikan_tamat_sd: Optional[int] = None
    pendidikan_tamat_sma: Optional[int] = None
    pendidikan_tamat_smp: Optional[int] = None
    pendidikan_tidak_sekolah: Optional[int] = None
    pendidikan_tidak_tamat_sd: Optional[int] = None
    status_bekerja_tidak_bekerja: Optional[int] = None
    status_bekerja_bekerja: Optional[int] = None
    pendapatan_keluarga_kategori_1: Optional[int] = None
    pendapatan_keluarga_kategori_2: Optional[int] = None
    pendapatan_keluarga_kategori_3: Optional[int] = None
    pendapatan_keluarga_kategori_4: Optional[int] = None
    pendapatan_keluarga_kategori_5: Optional[int] = None
    tpt_serumah_tidak_mendapatkan_tpt: Optional[int] = None
    tpt_serumah_tidak_ada: Optional[int] = None
    tpt_serumah_ada: Optional[int] = None
    perokok_aktif_tidak: Optional[int] = None
    perokok_aktif_ya: Optional[int] = None
    konsumsi_alkohol_tidak: Optional[int] = None
    konsumsi_alkohol_ya: Optional[int] = None
    kategori_pengetahuan_cukup: Optional[int] = None
    kategori_pengetahuan_kurang: Optional[int] = None
    kategori_pengetahuan_baik: Optional[int] = None
    kategori_pengetahuan_buruk: Optional[int] = None
    kategori_literasi_problematic: Optional[int] = None
    kategori_literasi_excellent: Optional[int] = None
    kategori_literasi_inadequate: Optional[int] = None
    kategori_literasi_sufficient: Optional[int] = None
    kategori_stigma_tinggi: Optional[int] = None
    kategori_stigma_sedang: Optional[int] = None
    kategori_stigma_rendah: Optional[int] = None
    kategori_stigma_tidak: Optional[int] = None


class SurveyCreate(SurveyBase):
    pass


class SurveyUpdate(SurveyBase):
    pass


class SurveyInDBBase(SurveyBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Survey(SurveyInDBBase):
    pass


class SurveyInDB(SurveyInDBBase):
    pass
