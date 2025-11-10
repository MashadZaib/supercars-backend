from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.services.port_service import PortService
from app.schemas.port_schema import PortCreate, PortRead

router = APIRouter()

@router.post("/", response_model=PortRead)
def create_port(payload: PortCreate, db: Session = Depends(get_db)):
    return PortService(db).create_port(payload)

@router.get("/", response_model=List[PortRead])
def list_ports(
    search: Optional[str] = Query(None, description="Search Port by name"),
    db: Session = Depends(get_db)
):
    return PortService(db).get_ports(search)
