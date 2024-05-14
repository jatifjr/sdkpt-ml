from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    kelurahan_domisili = Column(String(255))
    kode_fasyankes = Column(String(255))
    tahun = Column(Integer)
    bulan = Column(Integer)
    tipe_diagnosis = Column(String(255))
    anatomi_tb = Column(String(255))
    riwayat_hiv = Column(String(255))
    riwayat_dm = Column(String(255))
    panduan_obat = Column(String(255))
    sumber_obat = Column(String(255))
    status_pengobatan = Column(String(255))
    pengobatan_terakhir = Column(String(255))
