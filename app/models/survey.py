from datetime import datetime
from calendar import month_name

from sqlalchemy import Column, Integer, String, Float, DateTime, func

from app.db.base_class import Base


class Survey(Base):
    __tablename__ = "survey"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now(),
                        index=True, nullable=False)
    # Change String to Integer
    bulan = Column(Integer, index=True, nullable=False)
    tahun = Column(Integer, index=True, nullable=False)
    kelurahan_id = Column(Integer, index=True, nullable=False)
    kelurahan_name = Column(String(255), index=True, nullable=False)
    population_density = Column(Integer)
    population = Column(Integer)
    tb_cases = Column(Integer)
    population_tb_cases_ratio = Column(Float)
    dm_cases = Column(Integer)
    jumlah_klinik_pratama = Column(Integer)
    jumlah_klinik_utama = Column(Integer)
    gender_perempuan = Column(Integer)
    gender_laki_laki = Column(Integer)
    usia_paruh_baya = Column(Integer)
    usia_pensiun = Column(Integer)
    usia_pekerja_awal = Column(Integer)
    usia_lanjut = Column(Integer)
    usia_muda = Column(Integer)
    usia_pra_pensiun = Column(Integer)
    usia_anak = Column(Integer)
    pendidikan_diploma = Column(Integer)
    pendidikan_s1 = Column(Integer)
    pendidikan_s2_s3 = Column(Integer)
    pendidikan_tamat_sd = Column(Integer)
    pendidikan_tamat_sma = Column(Integer)
    pendidikan_tamat_smp = Column(Integer)
    pendidikan_tidak_sekolah = Column(Integer)
    pendidikan_tidak_tamat_sd = Column(Integer)
    status_bekerja_tidak_bekerja = Column(Integer)
    status_bekerja_bekerja = Column(Integer)
    pendapatan_keluarga_kategori_1 = Column(Integer)
    pendapatan_keluarga_kategori_2 = Column(Integer)
    pendapatan_keluarga_kategori_3 = Column(Integer)
    pendapatan_keluarga_kategori_4 = Column(Integer)
    pendapatan_keluarga_kategori_5 = Column(Integer)
    tpt_serumah_tidak_mendapatkan_tpt = Column(Integer)
    tpt_serumah_tidak_ada = Column(Integer)
    tpt_serumah_ada = Column(Integer)
    perokok_aktif_tidak = Column(Integer)
    perokok_aktif_ya = Column(Integer)
    konsumsi_alkohol_tidak = Column(Integer)
    konsumsi_alkohol_ya = Column(Integer)
    kategori_pengetahuan_cukup = Column(Integer)
    kategori_pengetahuan_kurang = Column(Integer)
    kategori_pengetahuan_baik = Column(Integer)
    kategori_pengetahuan_buruk = Column(Integer)
    kategori_literasi_problematic = Column(Integer)
    kategori_literasi_excellent = Column(Integer)
    kategori_literasi_inadequate = Column(Integer)
    kategori_literasi_sufficient = Column(Integer)
    kategori_stigma_tinggi = Column(Integer)
    kategori_stigma_sedang = Column(Integer)
    kategori_stigma_rendah = Column(Integer)
    kategori_stigma_tidak = Column(Integer)

    def __init__(self, **kwargs):
        bulan = kwargs.get('bulan')
        if bulan is not None and bulan != 0:
            self.bulan = bulan
        else:
            created_at_month = kwargs.get('created_at').month if kwargs.get(
                'created_at') else datetime.now().month
            # print("DEBUG - Created at month:", created_at_month)
            self.bulan = created_at_month

        tahun = kwargs.get('tahun')
        if tahun is not None and tahun != 0:
            self.tahun = tahun
        else:
            created_at_year = kwargs.get('created_at').year if kwargs.get(
                'created_at') else datetime.now().year
            # print("DEBUG - Created at year:", created_at_year)
            self.tahun = created_at_year

        super().__init__(**kwargs)
