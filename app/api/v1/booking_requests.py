from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.booking_request_schema import (
    BookingRequestCreate, BookingRequestRead, BookingRequestUpdate
)
from app.services.booking_request_service import BookingRequestService

router = APIRouter()

@router.post("/", response_model=BookingRequestRead, status_code=status.HTTP_201_CREATED)
def create_booking(payload: BookingRequestCreate, db: Session = Depends(db_session)):
    return BookingRequestService(db).create_booking(payload)

@router.get("/", response_model=List[BookingRequestRead])
def list_bookings(db: Session = Depends(db_session)):
    return BookingRequestService(db).list_bookings()

@router.get("/{booking_id}", response_model=BookingRequestRead)
def get_booking(booking_id: int, db: Session = Depends(db_session)):
    booking = BookingRequestService(db).get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking request not found")
    return booking

@router.put("/{booking_id}", response_model=BookingRequestRead)
def update_booking(booking_id: int, payload: BookingRequestUpdate, db: Session = Depends(db_session)):
    updated = BookingRequestService(db).update_booking(booking_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Booking request not found")
    return updated

@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(booking_id: int, db: Session = Depends(db_session)):
    ok = BookingRequestService(db).delete_booking(booking_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Booking request not found")
    return None
