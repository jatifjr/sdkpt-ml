from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Kelurahan(Base):
    __tablename__ = "kelurahan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    puskesmas_id = Column(Integer)
