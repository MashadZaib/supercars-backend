from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.cargo_description_schema import (
    CargoDescriptionCreate,
    CargoDescriptionRead,
    CargoDescriptionUpdate
)
from app.services.cargo_description_service import CargoDescriptionService

router = APIRouter()

@router.post("/", response_model=CargoDescriptionRead, status_code=status.HTTP_201_CREATED)
def create_description(payload: CargoDescriptionCreate, db: Session = Depends(db_session)):
    return CargoDescriptionService(db).create_description(payload)


@router.get("/", response_model=List[CargoDescriptionRead])
def list_descriptions(db: Session = Depends(db_session)):
    return CargoDescriptionService(db).list_descriptions()


@router.get("/{cargo_id}", response_model=CargoDescriptionRead)
def get_description(cargo_id: int, db: Session = Depends(db_session)):
    desc = CargoDescriptionService(db).get_description(cargo_id)
    if not desc:
        raise HTTPException(status_code=404, detail="Cargo description not found")
    return desc


@router.put("/{cargo_id}", response_model=CargoDescriptionRead)
def update_description(cargo_id: int, payload: CargoDescriptionUpdate, db: Session = Depends(db_session)):
    updated = CargoDescriptionService(db).update_description(cargo_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Cargo description not found")
    return updated


@router.delete("/{cargo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_description(cargo_id: int, db: Session = Depends(db_session)):
    ok = CargoDescriptionService(db).delete_description(cargo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Cargo description not found")
    return None
