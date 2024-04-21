from typing import Any, Optional, List

from pydantic import BaseModel


class InterventionBase(BaseModel):
    kelurahan_name: str
    puskesmas_id: int
    intervention_1: str
    intervention_2: str
    intervention_3: str
    intervention_4: str
    intervention_5: str
    intervention_6: str
    intervention_7: str


class InterventionCreate(InterventionBase):
    pass


class InterventionUpdate(InterventionBase):
    pass


class InterventionInDBBase(InterventionBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class InterventionResponse(BaseModel):
    id: Optional[int] = None
    kelurahan_name: str
    puskesmas_id: int
    interventions: List[str]  # List of interventions

    @classmethod
    def from_db(cls, db_intervention: InterventionInDBBase) -> 'InterventionResponse':
        interventions = [
            getattr(db_intervention, f'intervention_{i}')
            for i in range(1, 8)
            if getattr(db_intervention, f'intervention_{i}')
        ]
        return cls(
            id=db_intervention.id,
            kelurahan_name=db_intervention.kelurahan_name,
            puskesmas_id=db_intervention.puskesmas_id,
            interventions=interventions
        )


class InterventionResponseBody(BaseModel):
    isi_intervensi: str


class InterventionResponseList(BaseModel):
    interventions: List[InterventionResponseBody]
