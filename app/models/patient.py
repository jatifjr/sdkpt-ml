from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    kode_pasien = Column(String(255), index=True, nullable=False)
    umur = Column(Integer)
    jenis_kelamin = Column(String(255))
    kecamatan = Column(String(255))
    kelurahan_id = Column(Integer)
    status_pekerjaan = Column(String(255))
    fasyankes_id = Column(Integer)
