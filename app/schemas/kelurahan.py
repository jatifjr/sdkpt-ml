from typing import Any, Optional, List

from pydantic import BaseModel


class Kelurahan(BaseModel):
    id: int
    kode_kd: str
    kelurahan_name: str
    puskesmas_id: int

    class Config:
        from_attributes = True
