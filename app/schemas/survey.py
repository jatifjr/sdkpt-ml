from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class SurveyBase(BaseModel):
    kelurahan_id: int
    kelurahan_name: str
    bulan: Optional[int] = None
    tahun: Optional[int] = None
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


class SurveyCreate(BaseModel):
    kelurahan_id: int = Field(None, alias='ID Kelurahan')
    kelurahan_name: str = Field(None, alias='KECAMATAN')
    bulan: Optional[int] = Field(None, alias='Bulan')
    tahun: Optional[int] = Field(None, alias='Tahun')
    population_density: Optional[int] = Field(None, alias='Kepadatan Penduduk')
    population: Optional[int] = Field(None, alias='Jumlah Penduduk')
    tb_cases: Optional[int] = Field(None, alias='Jumlah Kasus TB')
    population_tb_cases_ratio: Optional[float] = Field(
        None, alias='rasio Pasien dan Jumlah Penduduk')
    dm_cases: Optional[int] = Field(None, alias='Jumlah Kasus DM')
    jumlah_klinik_pratama: Optional[int] = Field(
        None, alias='Jumlah Klinik Pratama')
    jumlah_klinik_utama: Optional[int] = Field(
        None, alias='Jumlah Klinik Utama')
    gender_perempuan: Optional[int] = Field(None, alias='Gender_Perempuan')
    gender_laki_laki: Optional[int] = Field(None, alias='Gender_Laki-laki')
    usia_paruh_baya: Optional[int] = Field(None, alias='Usia_Usia Paruh Baya')
    usia_pensiun: Optional[int] = Field(None, alias='Usia_Usia Pensiun')
    usia_pekerja_awal: Optional[int] = Field(
        None, alias='Usia_Usia Pekerja Awal')
    usia_lanjut: Optional[int] = Field(None, alias='Usia_Usia Lanjut')
    usia_muda: Optional[int] = Field(None, alias='Usia_Usia Muda')
    usia_pra_pensiun: Optional[int] = Field(
        None, alias='Usia_Usia Pra-Pensiun')
    usia_anak: Optional[int] = Field(None, alias='Usia_Usia Anak')
    pendidikan_diploma: Optional[int] = Field(None, alias='Pendidikan_diploma')
    pendidikan_s1: Optional[int] = Field(None, alias='Pendidikan_s1')
    pendidikan_s2_s3: Optional[int] = Field(None, alias='Pendidikan_s2/s3')
    pendidikan_tamat_sd: Optional[int] = Field(
        None, alias='Pendidikan_tamat sd')
    pendidikan_tamat_sma: Optional[int] = Field(
        None, alias='Pendidikan_tamat sma/sederajat')
    pendidikan_tamat_smp: Optional[int] = Field(
        None, alias='Pendidikan_tamat smp/sederajat')
    pendidikan_tidak_sekolah: Optional[int] = Field(
        None, alias='Pendidikan_tidak sekolah')
    pendidikan_tidak_tamat_sd: Optional[int] = Field(
        None, alias='Pendidikan_tidak tamat sd')
    status_bekerja_tidak_bekerja: Optional[int] = Field(
        None, alias='Status_Bekerja_tidak bekerja')
    status_bekerja_bekerja: Optional[int] = Field(
        None, alias='Status_Bekerja_bekerja')
    pendapatan_keluarga_kategori_1: Optional[int] = Field(
        None, alias='Pendapatan_Keluarga_Kategori 1')
    pendapatan_keluarga_kategori_2: Optional[int] = Field(
        None, alias='Pendapatan_Keluarga_Kategori 2')
    pendapatan_keluarga_kategori_3: Optional[int] = Field(
        None, alias='Pendapatan_Keluarga_Kategori 3')
    pendapatan_keluarga_kategori_4: Optional[int] = Field(
        None, alias='Pendapatan_Keluarga_Kategori 4')
    pendapatan_keluarga_kategori_5: Optional[int] = Field(
        None, alias='Pendapatan_Keluarga_Kategori 5')
    tpt_serumah_tidak_mendapatkan_tpt: Optional[int] = Field(
        None, alias='TPT_serumah_tidak mendapatkan TPT')
    tpt_serumah_tidak_ada: Optional[int] = Field(
        None, alias='TPT_serumah_tidak ada')
    tpt_serumah_ada: Optional[int] = Field(None, alias='TPT_serumah_ada')
    perokok_aktif_tidak: Optional[int] = Field(
        None, alias='perokok_aktif_tidak')
    perokok_aktif_ya: Optional[int] = Field(None, alias='perokok_aktif_ya')
    konsumsi_alkohol_tidak: Optional[int] = Field(
        None, alias='konsumsi_alkohol_tidak')
    konsumsi_alkohol_ya: Optional[int] = Field(
        None, alias='konsumsi_alkohol_ya')
    kategori_pengetahuan_cukup: Optional[int] = Field(
        None, alias='Kategori Pengetahuan_Cukup')
    kategori_pengetahuan_kurang: Optional[int] = Field(
        None, alias='Kategori Pengetahuan_Kurang')
    kategori_pengetahuan_baik: Optional[int] = Field(
        None, alias='Kategori Pengetahuan_Baik')
    kategori_pengetahuan_buruk: Optional[int] = Field(
        None, alias='Kategori Pengetahuan_Buruk')
    kategori_literasi_problematic: Optional[int] = Field(
        None, alias='Kategori_Literasi_Problematic')
    kategori_literasi_excellent: Optional[int] = Field(
        None, alias='Kategori_Literasi_Excellent')
    kategori_literasi_inadequate: Optional[int] = Field(
        None, alias='Kategori_Literasi_Inadequate')
    kategori_literasi_sufficient: Optional[int] = Field(
        None, alias='Kategori_Literasi_Sufficient')
    kategori_stigma_tinggi: Optional[int] = Field(
        None, alias='Kategori Stigma_Stigma Tinggi')
    kategori_stigma_sedang: Optional[int] = Field(
        None, alias='Kategori Stigma_Stigma Sedang')
    kategori_stigma_rendah: Optional[int] = Field(
        None, alias='Kategori Stigma_Stigma Rendah')
    kategori_stigma_tidak: Optional[int] = Field(
        None, alias='Kategori Stigma_Tidak Stigma')


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


class SurveyItem(BaseModel):
    created_at: Optional[datetime] = None
    bulan: Optional[str] = None
    tahun: Optional[int] = None
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


class SurveyData(BaseModel):
    kelurahan_id: int
    kelurahan_name: str
    surveys: Optional[list[SurveyItem]] = None


class SurveyResponse(BaseModel):
    status: str
    message: str
    data: Optional[SurveyData] = None
