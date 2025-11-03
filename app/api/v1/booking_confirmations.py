from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.booking_confirmation_schema import (
    BookingConfirmationCreate,
    BookingConfirmationRead,
    BookingConfirmationUpdate
)
from app.services.booking_confirmation_service import BookingConfirmationService

router = APIRouter()

@router.post("/", response_model=BookingConfirmationRead, status_code=status.HTTP_201_CREATED)
def create_confirmation(payload: BookingConfirmationCreate, db: Session = Depends(db_session)):
    return BookingConfirmationService(db).create_confirmation(payload)

@router.get("/", response_model=List[BookingConfirmationRead])
def list_confirmations(db: Session = Depends(db_session)):
    return BookingConfirmationService(db).list_confirmations()

@router.get("/{confirmation_id}", response_model=BookingConfirmationRead)
def get_confirmation(confirmation_id: int, db: Session = Depends(db_session)):
    confirmation = BookingConfirmationService(db).get_confirmation(confirmation_id)
    if not confirmation:
        raise HTTPException(status_code=404, detail="Booking confirmation not found")
    return confirmation

@router.put("/{confirmation_id}", response_model=BookingConfirmationRead)
def update_confirmation(confirmation_id: int, payload: BookingConfirmationUpdate, db: Session = Depends(db_session)):
    updated = BookingConfirmationService(db).update_confirmation(confirmation_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Booking confirmation not found")
    return updated

@router.delete("/{confirmation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_confirmation(confirmation_id: int, db: Session = Depends(db_session)):
    ok = BookingConfirmationService(db).delete_confirmation(confirmation_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Booking confirmation not found")
    return None
