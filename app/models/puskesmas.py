from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Puskesmas(Base):
    __tablename__ = "puskesmas"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
