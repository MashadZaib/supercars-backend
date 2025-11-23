from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.vessel_info_schema import (
    VesselInfoCreate,
    VesselInfoRead,
    VesselInfoUpdate
)
from app.services.vessel_info_service import VesselInfoService

router = APIRouter()

@router.post("/", response_model=VesselInfoRead, status_code=status.HTTP_201_CREATED)
def create_vessel(payload: VesselInfoCreate, db: Session = Depends(db_session)):
    return VesselInfoService(db).create_vessel(payload)

@router.get("/", response_model=List[VesselInfoRead])
def list_vessels(db: Session = Depends(db_session)):
    return VesselInfoService(db).list_vessels()

@router.get("/{vessel_id}", response_model=VesselInfoRead)
def get_vessel(vessel_id: int, db: Session = Depends(db_session)):
    vessel = VesselInfoService(db).get_vessel(vessel_id)
    if not vessel:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return vessel

@router.put("/{vessel_id}", response_model=VesselInfoRead)
def update_vessel(vessel_id: int, payload: VesselInfoUpdate, db: Session = Depends(db_session)):
    updated = VesselInfoService(db).update_vessel(vessel_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return updated

@router.delete("/{vessel_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vessel(vessel_id: int, db: Session = Depends(db_session)):
    ok = VesselInfoService(db).delete_vessel(vessel_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Carrier not found")
    return None
