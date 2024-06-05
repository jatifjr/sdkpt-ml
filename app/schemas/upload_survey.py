from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# Base schema
class SurveyBase(BaseModel):
    kelurahan_id: Optional[int]
    kecamatan: Optional[str]
    kelurahan: Optional[str]
    kepadatan_penduduk: Optional[int]
    jumlah_penduduk: Optional[int]
    jumlah_kasus_tb: Optional[int]
    rasio_pasien_dan_jumlah_penduduk: Optional[float]
    jumlah_kasus_dm: Optional[int]
    prevalensi_dm: Optional[float]
    jumlah_klinik_pratama: Optional[int]
    jumlah_klinik_utama: Optional[int]
    rasio_penduduk_dan_fasyankes: Optional[float]
    jumlah_puskemas: Optional[int]
    pasien_jenis_kelamin_laki_laki: Optional[int]
    pasien_jenis_kelamin_perempuan: Optional[int]
    pasien_pendidikan_terakhir_diploma: Optional[int]
    pasien_pendidikan_terakhir_s1: Optional[int]
    pasien_pendidikan_terakhir_s2_s3: Optional[int]
    pasien_pendidikan_terakhir_tamat_sd: Optional[int]
    pasien_pendidikan_terakhir_tamat_sma_sederajat: Optional[int]
    pasien_pendidikan_terakhir_tamat_smp_sederajat: Optional[int]
    pasien_pendidikan_terakhir_tidak_sekolah: Optional[int]
    pasien_pendidikan_terakhir_tidak_tamat_sd: Optional[int]
    pasien_status_bekerja_bekerja: Optional[int]
    pasien_status_bekerja_tidak_bekerja: Optional[int]
    pasien_status_bekerja_belum_bekerja: Optional[int]
    pasien_pendapatan_keluarga_kategori1: Optional[int]
    pasien_pendapatan_keluarga_kategori2: Optional[int]
    pasien_pendapatan_keluarga_kategori3: Optional[int]
    pasien_pendapatan_keluarga_kategori4: Optional[int]
    pasien_pendapatan_keluarga_kategori5: Optional[int]
    pasien_efek_samping_obat_tidak: Optional[int]
    pasien_efek_samping_obat_ya: Optional[int]
    pasien_pengaruh_pendapatan_tidak: Optional[int]
    pasien_pengaruh_pendapatan_ya: Optional[int]
    pasien_kategori_bmi_berat_badan_kurang: Optional[int]
    pasien_kategori_bmi_berat_badan_normal: Optional[int]
    pasien_kategori_bmi_kelebihan_berat_badan: Optional[int]
    pasien_kategori_bmi_obesitas_i: Optional[int]
    pasien_kategori_bmi_obesitas_ii: Optional[int]
    pasien_kategori_usia_anak_anak: Optional[int]
    pasien_kategori_usia_balita: Optional[int]
    pasien_kategori_usia_dewasa_akhir: Optional[int]
    pasien_kategori_usia_dewasa_awal: Optional[int]
    pasien_kategori_usia_lansia_akhir: Optional[int]
    pasien_kategori_usia_lansia_awal: Optional[int]
    pasien_kategori_usia_manula: Optional[int]
    pasien_kategori_usia_remaja_akhir: Optional[int]
    pasien_kategori_usia_remaja_awal: Optional[int]
    pasien_kategori_pengetahuan_baik: Optional[int]
    pasien_kategori_pengetahuan_buruk: Optional[int]
    pasien_kategori_pengetahuan_cukup: Optional[int]
    pasien_kategori_pengetahuan_kurang: Optional[int]
    pasien_kategori_perilaku_baik: Optional[int]
    pasien_kategori_perilaku_cukup: Optional[int]
    pasien_kategori_perilaku_kurang: Optional[int]
    pasien_kategori_perilaku_sangat_kurang: Optional[int]
    pasien_kategori_literasi_excellent: Optional[int]
    pasien_kategori_literasi_inadequate: Optional[int]
    pasien_kategori_literasi_problematic: Optional[int]
    pasien_kategori_literasi_sufficient: Optional[int]
    pasien_kategori_stigma_tidak_stigma: Optional[int]
    pasien_kategori_stigma_stigma_rendah: Optional[int]
    pasien_kategori_stigma_stigma_sangat_rendah: Optional[int]
    pasien_kategori_stigma_stigma_sedang: Optional[int]
    pasien_kategori_stigma_stigma_tinggi: Optional[int]
    keluarga_pendidikan_terakhir_diploma: Optional[int]
    keluarga_pendidikan_terakhir_s1: Optional[int]
    keluarga_pendidikan_terakhir_s2_s3: Optional[int]
    keluarga_pendidikan_terakhir_tamat_sd: Optional[int]
    keluarga_pendidikan_terakhir_tamat_sma_sederajat: Optional[int]
    keluarga_pendidikan_terakhir_tamat_smp_sederajat: Optional[int]
    keluarga_pendidikan_terakhir_tidak_sekolah: Optional[int]
    keluarga_pendidikan_terakhir_tidak_tamat_sd: Optional[int]
    keluarga_status_bekerja_bekerja: Optional[int]
    keluarga_status_bekerja_tidak_bekerja: Optional[int]
    keluarga_riwayat_tb_di_rumah_ada: Optional[int]
    keluarga_riwayat_tb_di_rumah_tidak_ada: Optional[int]
    keluarga_tpt_serumah_ada: Optional[int]
    keluarga_tpt_serumah_tidak_ada: Optional[int]
    keluarga_jenis_lantai_kayu: Optional[int]
    keluarga_jenis_lantai_tanah: Optional[int]
    keluarga_jenis_lantai_ubin_keramik_tegel: Optional[int]
    keluarga_cahaya_matahari_masuk_tidak: Optional[int]
    keluarga_cahaya_matahari_masuk_ya: Optional[int]
    keluarga_kategori_pengetahuan_baik: Optional[int]
    keluarga_kategori_pengetahuan_buruk: Optional[int]
    keluarga_kategori_pengetahuan_cukup: Optional[int]
    keluarga_kategori_pengetahuan_kurang: Optional[int]
    keluarga_kategori_literasi_inadequate: Optional[int]
    keluarga_kategori_literasi_problematic: Optional[int]
    keluarga_kategori_literasi_sufficient: Optional[int]
    keluarga_kategori_literasi_excellent: Optional[int]
    keluarga_kategori_stigma_stigma_rendah: Optional[int]
    keluarga_kategori_stigma_stigma_sangat_rendah: Optional[int]
    keluarga_kategori_stigma_stigma_sedang: Optional[int]
    keluarga_kategori_stigma_stigma_tinggi: Optional[int]
    keluarga_kategori_stigma_tidak_stigma: Optional[int]
    keluarga_kategori_perilaku_baik: Optional[int]
    keluarga_kategori_perilaku_cukup: Optional[int]
    keluarga_kategori_perilaku_kurang: Optional[int]
    keluarga_kategori_perilaku_sangat_kurang: Optional[int]
    masyarakat_pendidikan_terakhir_diploma: Optional[int]
    masyarakat_pendidikan_terakhir_s1: Optional[int]
    masyarakat_pendidikan_terakhir_s2_s3: Optional[int]
    masyarakat_pendidikan_terakhir_tamat_sd: Optional[int]
    masyarakat_pendidikan_terakhir_tamat_sma_sederajat: Optional[int]
    masyarakat_pendidikan_terakhir_tamat_smp_sederajat: Optional[int]
    masyarakat_pendidikan_terakhir_tidak_sekolah: Optional[int]
    masyarakat_pendidikan_terakhir_tidak_tamat_sd: Optional[int]
    masyarakat_status_perkajaan_bekerja: Optional[int]
    masyarakat_status_perkajaan_tidak_bekerja: Optional[int]
    masyarakat_kategori_pendapatan_kategori1: Optional[int]
    masyarakat_kategori_pendapatan_kategori2: Optional[int]
    masyarakat_kategori_pendapatan_kategori3: Optional[int]
    masyarakat_kategori_pendapatan_kategori4: Optional[int]
    masyarakat_kategori_pendapatan_kategori5: Optional[int]
    masyarakat_riwayat_tb_keluarga_ada: Optional[int]
    masyarakat_riwayat_tb_keluarga_tidak_ada: Optional[int]
    masyarakat_kategori_bmi_berat_badan_kurang: Optional[int]
    masyarakat_kategori_bmi_berat_badan_normal: Optional[int]
    masyarakat_kategori_bmi_kelebihan_berat_badan: Optional[int]
    masyarakat_kategori_bmi_obesitas_i: Optional[int]
    masyarakat_kategori_bmi_obesitas_ii: Optional[int]
    masyarakat_kategori_pengetahuan_baik: Optional[int]
    masyarakat_kategori_pengetahuan_buruk: Optional[int]
    masyarakat_kategori_pengetahuan_cukup: Optional[int]
    masyarakat_kategori_pengetahuan_kurang: Optional[int]
    masyarakat_kategori_perilaku_baik: Optional[int]
    masyarakat_kategori_perilaku_cukup: Optional[int]
    masyarakat_kategori_perilaku_kurang: Optional[int]
    masyarakat_kategori_perilaku_sangat_kurang: Optional[int]
    masyarakat_kategori_literasi_excellent: Optional[int]
    masyarakat_kategori_literasi_inadequate: Optional[int]
    masyarakat_kategori_literasi_problematic: Optional[int]
    masyarakat_kategori_literasi_sufficient: Optional[int]
    masyarakat_kategori_stigma_stigma_rendah: Optional[int]
    masyarakat_kategori_stigma_stigma_sangat_rendah: Optional[int]
    masyarakat_kategori_stigma_stigma_sedang: Optional[int]
    masyarakat_kategori_stigma_stigma_tinggi: Optional[int]
    masyarakat_kategori_stigma_tidak_stigma: Optional[int]


# Schema for creating a survey entry
class SurveyCreate(SurveyBase):
    pass


# Schema for reading a survey entry
class SurveyRead(SurveyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class SurveyData(BaseModel):
    kelurahan_id: int
    kelurahan_name: str
    surveys: Optional[list[SurveyBase]] = None


class SurveyResponse(BaseModel):
    status: str
    message: str
    data: Optional[SurveyData] = None


class SurveyLatest(BaseModel):
    kelurahan_id: Optional[int] = None
    kelurahan_name: Optional[str] = None
    bulan: Optional[str] = None
    tahun: Optional[int] = None
