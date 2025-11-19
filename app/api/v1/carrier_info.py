from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.carrier_info_schema import (
    CarrierInfoCreate,
    CarrierInfoRead,
    CarrierInfoUpdate
)
from app.services.carrier_info_service import CarrierInfoService

router = APIRouter()

@router.post("/", response_model=CarrierInfoRead, status_code=status.HTTP_201_CREATED)
def create_carrier(payload: CarrierInfoCreate, db: Session = Depends(db_session)):
    return CarrierInfoService(db).create_carrier(payload)

@router.get("/", response_model=List[CarrierInfoRead])
def list_carriers(db: Session = Depends(db_session)):
    return CarrierInfoService(db).list_carriers()

@router.get("/{carrier_id}", response_model=CarrierInfoRead)
def get_carrier(carrier_id: int, db: Session = Depends(db_session)):
    carrier = CarrierInfoService(db).get_carrier(carrier_id)
    if not carrier:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return carrier

@router.put("/{carrier_id}", response_model=CarrierInfoRead)
def update_carrier(carrier_id: int, payload: CarrierInfoUpdate, db: Session = Depends(db_session)):
    updated = CarrierInfoService(db).update_carrier(carrier_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return updated

@router.delete("/{carrier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carrier(carrier_id: int, db: Session = Depends(db_session)):
    ok = CarrierInfoService(db).delete_carrier(carrier_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return None
