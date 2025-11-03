from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.charge_schema import (
    ChargeCreate,
    ChargeRead,
    ChargeUpdate,
)
from app.services.charge_service import ChargeService

router = APIRouter()

@router.post("/", response_model=ChargeRead, status_code=status.HTTP_201_CREATED)
def create_charge(payload: ChargeCreate, db: Session = Depends(db_session)):
    return ChargeService(db).create_charge(payload)

@router.get("/", response_model=List[ChargeRead])
def list_charges(db: Session = Depends(db_session)):
    return ChargeService(db).list_charges()

@router.get("/{charge_id}", response_model=ChargeRead)
def get_charge(charge_id: int, db: Session = Depends(db_session)):
    charge = ChargeService(db).get_charge(charge_id)
    if not charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    return charge

@router.put("/{charge_id}", response_model=ChargeRead)
def update_charge(charge_id: int, payload: ChargeUpdate, db: Session = Depends(db_session)):
    updated = ChargeService(db).update_charge(charge_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Charge not found")
    return updated

@router.delete("/{charge_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_charge(charge_id: int, db: Session = Depends(db_session)):
    ok = ChargeService(db).delete_charge(charge_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Charge not found")
    return None
