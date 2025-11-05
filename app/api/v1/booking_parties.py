from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.services.booking_party_service import BookingPartyService
from app.schemas.booking_party_schema import BookingPartyCreate, BookingPartyRead

router = APIRouter()

@router.post("/", response_model=BookingPartyRead)
def create_booking_party(payload: BookingPartyCreate, db: Session = Depends(get_db)):
    return BookingPartyService(db).create_booking_party(payload)

@router.get("/", response_model=List[BookingPartyRead])
def list_booking_parties(
    search: Optional[str] = Query(None, description="Search booking party by name"),
    db: Session = Depends(get_db)
):
    return BookingPartyService(db).get_booking_parties(search)
