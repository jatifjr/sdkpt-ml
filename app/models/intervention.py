from sqlalchemy import Column, Integer, String, Text, JSON

from app.db.base_class import Base


class Intervention(Base):
    __tablename__ = "interventions"

    id = Column(Integer, primary_key=True, index=True)
    kelurahan_name = Column(String(255), index=True, nullable=False)
    puskesmas_id = Column(Integer)
    intervention_1 = Column(Text)
    intervention_2 = Column(Text)
    intervention_3 = Column(Text)
    intervention_4 = Column(Text)
    intervention_5 = Column(Text)
    intervention_6 = Column(Text)
    intervention_7 = Column(Text)
