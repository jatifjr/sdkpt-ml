from typing import Any, Optional, List

from pydantic import BaseModel


class PatientBase(BaseModel):
    kelurahan_domisili: Optional[str] = None
    kode_fasyankes: Optional[str] = None
    tahun: Optional[int] = None
    bulan: Optional[int] = None
    tipe_diagnosis: Optional[str] = None
    anatomi_tb: Optional[str] = None
    riwayat_hiv: Optional[str] = None
    riwayat_dm: Optional[str] = None
    panduan_obat: Optional[str] = None
    sumber_obat: Optional[str] = None
    status_pengobatan: Optional[str] = None
    pengobatan_terakhir: Optional[str] = None


class PatientCreate(BaseModel):
    id: Optional[str] = None
    kelurahan_domisili: Optional[str] = None
    kode_fasyankes: Optional[str] = None
    tahun: Optional[int] = None
    bulan: Optional[int] = None
    tipe_diagnosis: Optional[str] = None
    anatomi_tb: Optional[str] = None
    riwayat_hiv: Optional[str] = None
    riwayat_dm: Optional[str] = None
    panduan_obat: Optional[str] = None
    sumber_obat: Optional[str] = None
    status_pengobatan: Optional[str] = None
    pengobatan_terakhir: Optional[str] = None


class PatientResponse(PatientBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True
