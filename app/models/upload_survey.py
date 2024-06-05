from sqlalchemy import Column, Integer, String, Float, func, DateTime
from app.db.base_class import Base


class UploadSurvey(Base):
    __tablename__ = "survey_upload"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now(),
                        index=True, nullable=False)
    kelurahan_id = Column(Integer, index=True, nullable=False)
    kecamatan = Column(String(255), index=True, nullable=False)
    kelurahan = Column(String(255), index=True, nullable=False)
    kepadatan_penduduk = Column(Integer)
    jumlah_penduduk = Column(Integer)
    jumlah_kasus_tb = Column(Integer)
    rasio_pasien_dan_jumlah_penduduk = Column(Float)
    jumlah_kasus_dm = Column(Integer)
    prevalensi_dm = Column(Float)
    jumlah_klinik_pratama = Column(Integer)
    jumlah_klinik_utama = Column(Integer)
    rasio_penduduk_dan_fasyankes = Column(Float)
    jumlah_puskemas = Column(Integer)
    pasien_jenis_kelamin_laki_laki = Column(Integer)
    pasien_jenis_kelamin_perempuan = Column(Integer)
    pasien_pendidikan_terakhir_diploma = Column(Integer)
    pasien_pendidikan_terakhir_s1 = Column(Integer)
    pasien_pendidikan_terakhir_s2_s3 = Column(Integer)
    pasien_pendidikan_terakhir_tamat_sd = Column(Integer)
    pasien_pendidikan_terakhir_tamat_sma_sederajat = Column(Integer)
    pasien_pendidikan_terakhir_tamat_smp_sederajat = Column(Integer)
    pasien_pendidikan_terakhir_tidak_sekolah = Column(Integer)
    pasien_pendidikan_terakhir_tidak_tamat_sd = Column(Integer)
    pasien_status_bekerja_bekerja = Column(Integer)
    pasien_status_bekerja_tidak_bekerja = Column(Integer)
    pasien_status_bekerja_belum_bekerja = Column(Integer)
    pasien_pendapatan_keluarga_kategori1 = Column(Integer)
    pasien_pendapatan_keluarga_kategori2 = Column(Integer)
    pasien_pendapatan_keluarga_kategori3 = Column(Integer)
    pasien_pendapatan_keluarga_kategori4 = Column(Integer)
    pasien_pendapatan_keluarga_kategori5 = Column(Integer)
    pasien_efek_samping_obat_tidak = Column(Integer)
    pasien_efek_samping_obat_ya = Column(Integer)
    pasien_pengaruh_pendapatan_tidak = Column(Integer)
    pasien_pengaruh_pendapatan_ya = Column(Integer)
    pasien_kategori_bmi_berat_badan_kurang = Column(Integer)
    pasien_kategori_bmi_berat_badan_normal = Column(Integer)
    pasien_kategori_bmi_kelebihan_berat_badan = Column(Integer)
    pasien_kategori_bmi_obesitas_i = Column(Integer)
    pasien_kategori_bmi_obesitas_ii = Column(Integer)
    pasien_kategori_usia_anak_anak = Column(Integer)
    pasien_kategori_usia_balita = Column(Integer)
    pasien_kategori_usia_dewasa_akhir = Column(Integer)
    pasien_kategori_usia_dewasa_awal = Column(Integer)
    pasien_kategori_usia_lansia_akhir = Column(Integer)
    pasien_kategori_usia_lansia_awal = Column(Integer)
    pasien_kategori_usia_manula = Column(Integer)
    pasien_kategori_usia_remaja_akhir = Column(Integer)
    pasien_kategori_usia_remaja_awal = Column(Integer)
    pasien_kategori_pengetahuan_baik = Column(Integer)
    pasien_kategori_pengetahuan_buruk = Column(Integer)
    pasien_kategori_pengetahuan_cukup = Column(Integer)
    pasien_kategori_pengetahuan_kurang = Column(Integer)
    pasien_kategori_perilaku_baik = Column(Integer)
    pasien_kategori_perilaku_cukup = Column(Integer)
    pasien_kategori_perilaku_kurang = Column(Integer)
    pasien_kategori_perilaku_sangat_kurang = Column(Integer)
    pasien_kategori_literasi_excellent = Column(Integer)
    pasien_kategori_literasi_inadequate = Column(Integer)
    pasien_kategori_literasi_problematic = Column(Integer)
    pasien_kategori_literasi_sufficient = Column(Integer)
    pasien_kategori_stigma_tidak_stigma = Column(Integer)
    pasien_kategori_stigma_stigma_rendah = Column(Integer)
    pasien_kategori_stigma_stigma_sangat_rendah = Column(Integer)
    pasien_kategori_stigma_stigma_sedang = Column(Integer)
    pasien_kategori_stigma_stigma_tinggi = Column(Integer)
    keluarga_pendidikan_terakhir_diploma = Column(Integer)
    keluarga_pendidikan_terakhir_s1 = Column(Integer)
    keluarga_pendidikan_terakhir_s2_s3 = Column(Integer)
    keluarga_pendidikan_terakhir_tamat_sd = Column(Integer)
    keluarga_pendidikan_terakhir_tamat_sma_sederajat = Column(Integer)
    keluarga_pendidikan_terakhir_tamat_smp_sederajat = Column(Integer)
    keluarga_pendidikan_terakhir_tidak_sekolah = Column(Integer)
    keluarga_pendidikan_terakhir_tidak_tamat_sd = Column(Integer)
    keluarga_status_bekerja_bekerja = Column(Integer)
    keluarga_status_bekerja_tidak_bekerja = Column(Integer)
    keluarga_riwayat_tb_di_rumah_ada = Column(Integer)
    keluarga_riwayat_tb_di_rumah_tidak_ada = Column(Integer)
    keluarga_tpt_serumah_ada = Column(Integer)
    keluarga_tpt_serumah_tidak_ada = Column(Integer)
    keluarga_jenis_lantai_kayu = Column(Integer)
    keluarga_jenis_lantai_tanah = Column(Integer)
    keluarga_jenis_lantai_ubin_keramik_tegel = Column(Integer)
    keluarga_cahaya_matahari_masuk_tidak = Column(Integer)
    keluarga_cahaya_matahari_masuk_ya = Column(Integer)
    keluarga_kategori_pengetahuan_baik = Column(Integer)
    keluarga_kategori_pengetahuan_buruk = Column(Integer)
    keluarga_kategori_pengetahuan_cukup = Column(Integer)
    keluarga_kategori_pengetahuan_kurang = Column(Integer)
    keluarga_kategori_literasi_inadequate = Column(Integer)
    keluarga_kategori_literasi_problematic = Column(Integer)
    keluarga_kategori_literasi_sufficient = Column(Integer)
    keluarga_kategori_literasi_excellent = Column(Integer)
    keluarga_kategori_stigma_stigma_rendah = Column(Integer)
    keluarga_kategori_stigma_stigma_sangat_rendah = Column(Integer)
    keluarga_kategori_stigma_stigma_sedang = Column(Integer)
    keluarga_kategori_stigma_stigma_tinggi = Column(Integer)
    keluarga_kategori_stigma_tidak_stigma = Column(Integer)
    keluarga_kategori_perilaku_baik = Column(Integer)
    keluarga_kategori_perilaku_cukup = Column(Integer)
    keluarga_kategori_perilaku_kurang = Column(Integer)
    keluarga_kategori_perilaku_sangat_kurang = Column(Integer)
    masyarakat_pendidikan_terakhir_diploma = Column(Integer)
    masyarakat_pendidikan_terakhir_s1 = Column(Integer)
    masyarakat_pendidikan_terakhir_s2_s3 = Column(Integer)
    masyarakat_pendidikan_terakhir_tamat_sd = Column(Integer)
    masyarakat_pendidikan_terakhir_tamat_sma_sederajat = Column(Integer)
    masyarakat_pendidikan_terakhir_tamat_smp_sederajat = Column(Integer)
    masyarakat_pendidikan_terakhir_tidak_sekolah = Column(Integer)
    masyarakat_pendidikan_terakhir_tidak_tamat_sd = Column(Integer)
    masyarakat_status_perkajaan_bekerja = Column(Integer)
    masyarakat_status_perkajaan_tidak_bekerja = Column(Integer)
    masyarakat_kategori_pendapatan_kategori1 = Column(Integer)
    masyarakat_kategori_pendapatan_kategori2 = Column(Integer)
    masyarakat_kategori_pendapatan_kategori3 = Column(Integer)
    masyarakat_kategori_pendapatan_kategori4 = Column(Integer)
    masyarakat_kategori_pendapatan_kategori5 = Column(Integer)
    masyarakat_riwayat_tb_keluarga_ada = Column(Integer)
    masyarakat_riwayat_tb_keluarga_tidak_ada = Column(Integer)
    masyarakat_kategori_bmi_berat_badan_kurang = Column(Integer)
    masyarakat_kategori_bmi_berat_badan_normal = Column(Integer)
    masyarakat_kategori_bmi_kelebihan_berat_badan = Column(Integer)
    masyarakat_kategori_bmi_obesitas_i = Column(Integer)
    masyarakat_kategori_bmi_obesitas_ii = Column(Integer)
    masyarakat_kategori_pengetahuan_baik = Column(Integer)
    masyarakat_kategori_pengetahuan_buruk = Column(Integer)
    masyarakat_kategori_pengetahuan_cukup = Column(Integer)
    masyarakat_kategori_pengetahuan_kurang = Column(Integer)
    masyarakat_kategori_perilaku_baik = Column(Integer)
    masyarakat_kategori_perilaku_cukup = Column(Integer)
    masyarakat_kategori_perilaku_kurang = Column(Integer)
    masyarakat_kategori_perilaku_sangat_kurang = Column(Integer)
    masyarakat_kategori_literasi_excellent = Column(Integer)
    masyarakat_kategori_literasi_inadequate = Column(Integer)
    masyarakat_kategori_literasi_problematic = Column(Integer)
    masyarakat_kategori_literasi_sufficient = Column(Integer)
    masyarakat_kategori_stigma_stigma_rendah = Column(Integer)
    masyarakat_kategori_stigma_stigma_sangat_rendah = Column(Integer)
    masyarakat_kategori_stigma_stigma_sedang = Column(Integer)
    masyarakat_kategori_stigma_stigma_tinggi = Column(Integer)
    masyarakat_kategori_stigma_tidak_stigma = Column(Integer)