from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.services.cargo_type_service import CargoTypeService
from app.schemas.cargo_type_schema import CargoTypeCreate, CargoTypeRead

router = APIRouter()

@router.post("/", response_model=CargoTypeRead)
def create_cargo_type(payload: CargoTypeCreate, db: Session = Depends(get_db)):
    return CargoTypeService(db).create_cargo_type(payload)

@router.get("/", response_model=List[CargoTypeRead])
def list_cargo_types(
    search: Optional[str] = Query(None, description="Search Cargo Type by name"),
    db: Session = Depends(get_db)
):
    return CargoTypeService(db).get_cargo_types(search)
