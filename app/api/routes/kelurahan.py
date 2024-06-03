from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.api import deps
from app.crud import kelurahan as kelurahan_crud

router = APIRouter()


@router.get("/ref", response_model=schemas.Kelurahan)
def get_kode_kd_by_kelurahan_id(
    kelurahan_id: int,
    db: Session = Depends(deps.get_db)
) -> schemas.Kelurahan:
    res = kelurahan_crud.get_by_kelurahan_id(db, kelurahan_id)
    if not res:
        raise HTTPException(status_code=404, detail="Kelurahan not found")
    return res
