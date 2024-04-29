from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Kecamatan(Base):
    __tablename__ = "kecamatan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
