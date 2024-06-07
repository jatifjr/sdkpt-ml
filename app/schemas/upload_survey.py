from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


# Base schema
class SurveyBase(BaseModel):
    kelurahan_id: Optional[int] = Field(alias="ID Kelurahan")
    kecamatan: Optional[str] = Field(alias="Kecamatan")
    kelurahan: Optional[str] = Field(alias="Kelurahan")
    kepadatan_penduduk: Optional[int] = Field(alias="Kepadatan Penduduk")
    jumlah_penduduk: Optional[int] = Field(alias="Jumlah Penduduk")
    jumlah_kasus_tb: Optional[int] = Field(alias="Jumlah Kasus TB")
    rasio_pasien_dan_jumlah_penduduk: Optional[float] = Field(
        alias="rasio Pasien dan Jumlah Penduduk/10000")
    jumlah_kasus_dm: Optional[int] = Field(alias="Jumlah Kasus DM")
    prevalensi_dm: Optional[float] = Field(alias="Prevalensi DM/1000")
    jumlah_klinik_pratama: Optional[int] = Field(alias="Jumlah Klinik Pratama")
    jumlah_klinik_utama: Optional[int] = Field(alias="Jumlah Klinik Utama")
    rasio_penduduk_dan_fasyankes: Optional[float] = Field(
        alias="Rasio penduduk dengan Fasyankes")
    jumlah_puskemas: Optional[int] = Field(
        alias="Jumlah Puskesmas (Jadi satu dengan klinik untuk rasio)")
    pasien_jenis_kelamin_laki_laki: Optional[int] = Field(
        alias="Pasien_JenisKelamin_Laki-laki")
    pasien_jenis_kelamin_perempuan: Optional[int] = Field(
        alias="Pasien_JenisKelamin_Perempuan")
    pasien_pendidikan_terakhir_diploma: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_Diploma")
    pasien_pendidikan_terakhir_s1: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_S1")
    pasien_pendidikan_terakhir_s2_s3: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_S2/S3")
    pasien_pendidikan_terakhir_tamat_sd: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_TamatSD")
    pasien_pendidikan_terakhir_tamat_sma_sederajat: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_TamatSMA/Sederajat")
    pasien_pendidikan_terakhir_tamat_smp_sederajat: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_TamatSMP/Sederajat")
    pasien_pendidikan_terakhir_tidak_sekolah: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_TidakSekolah")
    pasien_pendidikan_terakhir_tidak_tamat_sd: Optional[int] = Field(
        alias="Pasien_PendidikanTerakhir_TidakTamatSD")
    pasien_status_bekerja_bekerja: Optional[int] = Field(
        alias="Pasien_StatusBekerja_Bekerja")
    pasien_status_bekerja_tidak_bekerja: Optional[int] = Field(
        alias="Pasien_StatusBekerja_TidakBekerja")
    pasien_status_bekerja_belum_bekerja: Optional[int] = Field(
        alias="Pasien_StatusBekerja_BelumBekerja")
    pasien_pendapatan_keluarga_kategori1: Optional[int] = Field(
        alias="Pasien_PendapatanKeluarga_Kategori1")
    pasien_pendapatan_keluarga_kategori2: Optional[int] = Field(
        alias="Pasien_PendapatanKeluarga_Kategori2")
    pasien_pendapatan_keluarga_kategori3: Optional[int] = Field(
        alias="Pasien_PendapatanKeluarga_Kategori3")
    pasien_pendapatan_keluarga_kategori4: Optional[int] = Field(
        alias="Pasien_PendapatanKeluarga_kategori4")
    pasien_pendapatan_keluarga_kategori5: Optional[int] = Field(
        alias="Pasien_PendapatanKeluarga_Kategori5")
    pasien_efek_samping_obat_tidak: Optional[int] = Field(
        alias="Pasien_EfekSampingObat_Tidak")
    pasien_efek_samping_obat_ya: Optional[int] = Field(
        alias="Pasien_EfekSampingObat_Ya")
    pasien_pengaruh_pendapatan_tidak: Optional[int] = Field(
        alias="Pasien_PengaruhPendapatan_Tidak")
    pasien_pengaruh_pendapatan_ya: Optional[int] = Field(
        alias="Pasien_PengaruhPendapatan_Ya")
    pasien_kategori_bmi_berat_badan_kurang: Optional[int] = Field(
        alias="Pasien_KategoriBMI_BeratBadanKurang")
    pasien_kategori_bmi_berat_badan_normal: Optional[int] = Field(
        alias="Pasien_KategoriBMI_BeratBadanNormal")
    pasien_kategori_bmi_kelebihan_berat_badan: Optional[int] = Field(
        alias="Pasien_KategoriBMI_KelebihanBeratBadan")
    pasien_kategori_bmi_obesitas_i: Optional[int] = Field(
        alias="Pasien_KategoriBMI_obesitasI")
    pasien_kategori_bmi_obesitas_ii: Optional[int] = Field(
        alias="Pasien_KategoriBMI_obesitasII")
    pasien_kategori_usia_anak_anak: Optional[int] = Field(
        alias="Pasien_KategoriUsia_Anak-Anak")
    pasien_kategori_usia_balita: Optional[int] = Field(
        alias="Pasien_KategoriUsia_Balita")
    pasien_kategori_usia_dewasa_akhir: Optional[int] = Field(
        alias="Pasien_KategoriUsia_DewasaAkhir")
    pasien_kategori_usia_dewasa_awal: Optional[int] = Field(
        alias="Pasien_KategoriUsia_DewasaAwal")
    pasien_kategori_usia_lansia_akhir: Optional[int] = Field(
        alias="Pasien_KategoriUsia_LansiaAkhir")
    pasien_kategori_usia_lansia_awal: Optional[int] = Field(
        alias="Pasien_KategoriUsia_LansiaAwal")
    pasien_kategori_usia_manula: Optional[int] = Field(
        alias="Pasien_KategoriUsia_Manula")
    pasien_kategori_usia_remaja_akhir: Optional[int] = Field(
        alias="Pasien_KategoriUsia_RemajaAkhir")
    pasien_kategori_usia_remaja_awal: Optional[int] = Field(
        alias="Pasien_KategoriUsia_RemajaAwal")
    pasien_kategori_pengetahuan_baik: Optional[int] = Field(
        alias="Pasien_KategoriPengetahuan_Baik")
    pasien_kategori_pengetahuan_buruk: Optional[int] = Field(
        alias="Pasien_KategoriPengetahuan_Buruk")
    pasien_kategori_pengetahuan_cukup: Optional[int] = Field(
        alias="Pasien_KategoriPengetahuan_Cukup")
    pasien_kategori_pengetahuan_kurang: Optional[int] = Field(
        alias="Pasien_KategoriPengetahuan_Kurang")
    pasien_kategori_perilaku_baik: Optional[int] = Field(
        alias="Pasien_KategoriPerilaku_Baik")
    pasien_kategori_perilaku_cukup: Optional[int] = Field(
        alias="Pasien_KategoriPerilaku_Cukup")
    pasien_kategori_perilaku_kurang: Optional[int] = Field(
        alias="Pasien_KategoriPerilaku_Kurang")
    pasien_kategori_perilaku_sangat_kurang: Optional[int] = Field(
        alias="Pasien_KategoriPerilaku_SangatKurang")
    pasien_kategori_literasi_excellent: Optional[int] = Field(
        alias="Pasien_KategoriLiterasi_Excellent")
    pasien_kategori_literasi_inadequate: Optional[int] = Field(
        alias="Pasien_KategoriLiterasi_Inadequate")
    pasien_kategori_literasi_problematic: Optional[int] = Field(
        alias="Pasien_KategoriLiterasi_Problematic")
    pasien_kategori_literasi_sufficient: Optional[int] = Field(
        alias="Pasien_KategoriLiterasi_Sufficient")
    pasien_kategori_stigma_tidak_stigma: Optional[int] = Field(
        alias="Pasien_KategoriStigma_TidakStigma")
    pasien_kategori_stigma_stigma_rendah: Optional[int] = Field(
        alias="Pasien_KategoriStigma_StigmaRendah")
    pasien_kategori_stigma_stigma_sangat_rendah: Optional[int] = Field(
        alias="Pasien_KategoriStigma_StigmaSangatRendah")
    pasien_kategori_stigma_stigma_sedang: Optional[int] = Field(
        alias="Pasien_KategoriStigma_StigmaSedang")
    pasien_kategori_stigma_stigma_tinggi: Optional[int] = Field(
        alias="Pasien_KategoriStigma_StigmaTinggi")
    keluarga_pendidikan_terakhir_diploma: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_Diploma")
    keluarga_pendidikan_terakhir_s1: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_S1")
    keluarga_pendidikan_terakhir_s2_s3: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_S2/S3")
    keluarga_pendidikan_terakhir_tamat_sd: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_TamatSD")
    keluarga_pendidikan_terakhir_tamat_sma_sederajat: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_TamatSMA/Sederajat")
    keluarga_pendidikan_terakhir_tamat_smp_sederajat: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_TamatSMP/Sederajat")
    keluarga_pendidikan_terakhir_tidak_sekolah: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_TidakSekolah")
    keluarga_pendidikan_terakhir_tidak_tamat_sd: Optional[int] = Field(
        alias="Keluarga_PendidikanTerakhir_TidakTamatSD")
    keluarga_status_bekerja_bekerja: Optional[int] = Field(
        alias="Keluarga_StatusBekerja_Bekerja")
    keluarga_status_bekerja_tidak_bekerja: Optional[int] = Field(
        alias="Keluarga_StatusBekerja_TidakBekerja")
    keluarga_riwayat_tb_di_rumah_ada: Optional[int] = Field(
        alias="Keluarga_RiwayatTBdiRumah_Ada")
    keluarga_riwayat_tb_di_rumah_tidak_ada: Optional[int] = Field(
        alias="Keluarga_RiwayatTBdiRumah_TidakAda")
    keluarga_tpt_serumah_ada: Optional[int] = Field(
        alias="Keluarga_TPTSerumah_Ada")
    keluarga_tpt_serumah_tidak_ada: Optional[int] = Field(
        alias="Keluarga_TPTSerumah_TidakAda")
    keluarga_jenis_lantai_kayu: Optional[int] = Field(
        alias="Keluarga_JenisLantai_Kayu")
    keluarga_jenis_lantai_tanah: Optional[int] = Field(
        alias="Keluarga_JenisLantai_Tanah")
    keluarga_jenis_lantai_ubin_keramik_tegel: Optional[int] = Field(
        alias="Keluarga_JenisLantai_Ubin/keramik/tegel")
    keluarga_cahaya_matahari_masuk_tidak: Optional[int] = Field(
        alias="Keluarga_CahayaMataharimasuk_Tidak")
    keluarga_cahaya_matahari_masuk_ya: Optional[int] = Field(
        alias="Keluarga_CahayaMataharimasuk_Ya")
    keluarga_kategori_pengetahuan_baik: Optional[int] = Field(
        alias="Keluarga_KategoriPengetahuan_Baik")
    keluarga_kategori_pengetahuan_buruk: Optional[int] = Field(
        alias="Keluarga_KategoriPengetahuan_Buruk")
    keluarga_kategori_pengetahuan_cukup: Optional[int] = Field(
        alias="Keluarga_KategoriPengetahuan_Cukup")
    keluarga_kategori_pengetahuan_kurang: Optional[int] = Field(
        alias="Keluarga_KategoriPengetahuan_Kurang")
    keluarga_kategori_literasi_inadequate: Optional[int] = Field(
        alias="Keluarga_KategoriLiterasi_Inadequate")
    keluarga_kategori_literasi_problematic: Optional[int] = Field(
        alias="Keluarga_KategoriLiterasi_Problematic")
    keluarga_kategori_literasi_sufficient: Optional[int] = Field(
        alias="Keluarga_KategoriLiterasi_Sufficient")
    keluarga_kategori_literasi_excellent: Optional[int] = Field(
        alias="Keluarga_KategoriLiterasi_Excellent")
    keluarga_kategori_stigma_stigma_rendah: Optional[int] = Field(
        alias="Keluarga_KategoriStigma_StigmaRendah")
    keluarga_kategori_stigma_stigma_sangat_rendah: Optional[int] = Field(
        alias="Keluarga_KategoriStigma_StigmaSangatRendah")
    keluarga_kategori_stigma_stigma_sedang: Optional[int] = Field(
        alias="Keluarga_KategoriStigma_StigmaSedang")
    keluarga_kategori_stigma_stigma_tinggi: Optional[int] = Field(
        alias="Keluarga_KategoriStigma_StigmaTinggi")
    keluarga_kategori_stigma_tidak_stigma: Optional[int] = Field(
        alias="Keluarga_KategoriStigma_TidakStigma")
    keluarga_kategori_perilaku_baik: Optional[int] = Field(
        alias="Keluarga_KategoriPerilaku_Baik")
    keluarga_kategori_perilaku_cukup: Optional[int] = Field(
        alias="Keluarga_KategoriPerilaku_Cukup")
    keluarga_kategori_perilaku_kurang: Optional[int] = Field(
        alias="Keluarga_KategoriPerilaku_Kurang")
    keluarga_kategori_perilaku_sangat_kurang: Optional[int] = Field(
        alias="Keluarga_KategoriPerilaku_SangatKurang")
    masyarakat_pendidikan_terakhir_diploma: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_Diploma")
    masyarakat_pendidikan_terakhir_s1: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_S1")
    masyarakat_pendidikan_terakhir_s2_s3: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_S2/S3")
    masyarakat_pendidikan_terakhir_tamat_sd: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_TamatSD")
    masyarakat_pendidikan_terakhir_tamat_sma_sederajat: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_TamatSMA/Sederajat")
    masyarakat_pendidikan_terakhir_tamat_smp_sederajat: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_TamatSMP/Sederajat")
    masyarakat_pendidikan_terakhir_tidak_sekolah: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_TidakSekolah")
    masyarakat_pendidikan_terakhir_tidak_tamat_sd: Optional[int] = Field(
        alias="Masyarakat_PendidikanTerakhir_TidakTamatSD")
    masyarakat_status_perkajaan_bekerja: Optional[int] = Field(
        alias="Masyarakat_StatusPerkajaan_Bekerja")
    masyarakat_status_perkajaan_tidak_bekerja: Optional[int] = Field(
        alias="Masyarakat_StatusPerkajaan_TidakBekerja")
    masyarakat_kategori_pendapatan_kategori1: Optional[int] = Field(
        alias="Masyarakat_KategoriPendapatan_Kategori1")
    masyarakat_kategori_pendapatan_kategori2: Optional[int] = Field(
        alias="Masyarakat_KategoriPendapatan_Kategori2")
    masyarakat_kategori_pendapatan_kategori3: Optional[int] = Field(
        alias="Masyarakat_KategoriPendapatan_Kategori3")
    masyarakat_kategori_pendapatan_kategori4: Optional[int] = Field(
        alias="Masyarakat_KategoriPendapatan_kategori4")
    masyarakat_kategori_pendapatan_kategori5: Optional[int] = Field(
        alias="Masyarakat_KategoriPendapatan_Kategori5")
    masyarakat_riwayat_tb_keluarga_ada: Optional[int] = Field(
        alias="Masyarakat_RiwayatTBKeluarga_Ada")
    masyarakat_riwayat_tb_keluarga_tidak_ada: Optional[int] = Field(
        alias="Masyarakat_RiwayatTBKeluarga_TidakAda")
    masyarakat_kategori_bmi_berat_badan_kurang: Optional[int] = Field(
        alias="Masyarakat_KategoriBMI_BeratBadanKurang")
    masyarakat_kategori_bmi_berat_badan_normal: Optional[int] = Field(
        alias="Masyarakat_KategoriBMI_BeratBadanNormal")
    masyarakat_kategori_bmi_kelebihan_berat_badan: Optional[int] = Field(
        alias="Masyarakat_KategoriBMI_KelebihanBeratBadan")
    masyarakat_kategori_bmi_obesitas_i: Optional[int] = Field(
        alias="Masyarakat_KategoriBMI_obesitasI")
    masyarakat_kategori_bmi_obesitas_ii: Optional[int] = Field(
        alias="Masyarakat_KategoriBMI_obesitasII")
    masyarakat_kategori_pengetahuan_baik: Optional[int] = Field(
        alias="Masyarakat_KategoriPengetahuan_Baik")
    masyarakat_kategori_pengetahuan_buruk: Optional[int] = Field(
        alias="Masyarakat_KategoriPengetahuan_Buruk")
    masyarakat_kategori_pengetahuan_cukup: Optional[int] = Field(
        alias="Masyarakat_KategoriPengetahuan_Cukup")
    masyarakat_kategori_pengetahuan_kurang: Optional[int] = Field(
        alias="Masyarakat_KategoriPengetahuan_Kurang")
    masyarakat_kategori_perilaku_baik: Optional[int] = Field(
        alias="Masyarakat_KategoriPerilaku_Baik")
    masyarakat_kategori_perilaku_cukup: Optional[int] = Field(
        alias="Masyarakat_KategoriPerilaku_Cukup")
    masyarakat_kategori_perilaku_kurang: Optional[int] = Field(
        alias="Masyarakat_KategoriPerilaku_Kurang")
    masyarakat_kategori_perilaku_sangat_kurang: Optional[int] = Field(
        alias="Masyarakat_KategoriPerilaku_SangatKurang")
    masyarakat_kategori_literasi_excellent: Optional[int] = Field(
        alias="Masyarakat_KategoriLiterasi_Excellent")
    masyarakat_kategori_literasi_inadequate: Optional[int] = Field(
        alias="Masyarakat_KategoriLiterasi_Inadequate")
    masyarakat_kategori_literasi_problematic: Optional[int] = Field(
        alias="Masyarakat_KategoriLiterasi_Problematic")
    masyarakat_kategori_literasi_sufficient: Optional[int] = Field(
        alias="Masyarakat_KategoriLiterasi_Sufficient")
    masyarakat_kategori_stigma_stigma_rendah: Optional[int] = Field(
        alias="Masyarakat_KategoriStigma_StigmaRendah")
    masyarakat_kategori_stigma_stigma_sangat_rendah: Optional[int] = Field(
        alias="Masyarakat_KategoriStigma_StigmaSangatRendah")
    masyarakat_kategori_stigma_stigma_sedang: Optional[int] = Field(
        alias="Masyarakat_KategoriStigma_StigmaSedang")
    masyarakat_kategori_stigma_stigma_tinggi: Optional[int] = Field(
        alias="Masyarakat_KategoriStigma_StigmaTinggi")
    masyarakat_kategori_stigma_tidak_stigma: Optional[int] = Field(
        alias="Masyarakat_KategoriStigma_TidakStigma")


# Schema for creating a survey entry
class SurveyCreate(SurveyBase):
    pass


class SurveyItem(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
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


# Schema for reading a survey entry
class SurveyInDBBase(SurveyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class SurveyData(BaseModel):
    kelurahan_id: int
    kelurahan_name: str
    surveys: Optional[list[SurveyItem]] = None


class SurveyResponse(BaseModel):
    status: str
    message: str
    data: Optional[SurveyData] = None


class SurveyLatest(BaseModel):
    kelurahan_id: Optional[int] = None
    kelurahan_name: Optional[str] = None
    bulan: Optional[str] = None
    tahun: Optional[int] = None
