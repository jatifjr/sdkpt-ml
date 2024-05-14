from sqlalchemy import Column, String, Text, DateTime, func

from app.db.base_class import Base


class SemarBetulAuth(Base):
    __tablename__ = "semar_betul_auth"

    id = Column(String(255), primary_key=True, index=True)
    access_token = Column(Text(2048), index=True, nullable=False)
