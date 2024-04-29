from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Fasyankes(Base):
    __tablename__ = "fasyankes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), index=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    province = Column(String(255))
    city = Column(String(255))
    type = Column(String(255))
    ownership = Column(String(255))
