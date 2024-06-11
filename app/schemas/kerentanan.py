from typing import List, Optional

from pydantic import BaseModel


class KerentananBase(BaseModel):
    kelurahan: str
    jumlah_kasus: int
    kategori_kerentanan: str


class KerentananCreate(KerentananBase):
    pass


class KerentananUpdate(KerentananBase):
    pass


class Kerentanan(KerentananBase):
    id: int

    class Config:
        from_attributes: True
