from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Kerentanan(Base):
    __tablename__ = "kerentanan"

    id = Column(Integer, primary_key=True, index=True)
    kelurahan = Column(String(255), index=True, nullable=False)
    jumlah_kasus = Column(Integer)
    kategori_kerentanan = Column(String(255), index=True, nullable=False)
