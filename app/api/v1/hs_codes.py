from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.hs_code_schema import HsCodeCreate, HsCodeRead, HsCodeUpdate
from app.services.hs_code_service import HsCodeService

router = APIRouter()


@router.post("/", response_model=HsCodeRead, status_code=status.HTTP_201_CREATED)
def create_hs_code(payload: HsCodeCreate, db: Session = Depends(db_session)):
    return HsCodeService(db).create_hs_code(payload)


@router.get("/", response_model=List[HsCodeRead])
def list_hs_codes(db: Session = Depends(db_session)):
    return HsCodeService(db).list_hs_codes()


@router.get("/{hs_code_id}", response_model=HsCodeRead)
def get_hs_code(hs_code_id: int, db: Session = Depends(db_session)):
    hs_obj = HsCodeService(db).get_hs_code(hs_code_id)
    if not hs_obj:
        raise HTTPException(status_code=404, detail="HS Code not found")
    return hs_obj


@router.put("/{hs_code_id}", response_model=HsCodeRead)
def update_hs_code(hs_code_id: int, payload: HsCodeUpdate, db: Session = Depends(db_session)):
    updated = HsCodeService(db).update_hs_code(hs_code_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="HS Code not found")
    return updated


@router.delete("/{hs_code_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hs_code(hs_code_id: int, db: Session = Depends(db_session)):
    ok = HsCodeService(db).delete_hs_code(hs_code_id)
    if not ok:
        raise HTTPException(status_code=404, detail="HS Code not found")
    return None
