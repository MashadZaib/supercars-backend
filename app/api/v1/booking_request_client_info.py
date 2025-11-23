from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import db_session
from app.schemas.booking_request_client_info_schema import (
    BookingRequestClientInfoCreate,
    BookingRequestClientInfoRead,
)
from app.services.booking_request_client_info_service import (
    BookingRequestClientInfoService,
)

router = APIRouter()


@router.post("/", response_model=BookingRequestClientInfoRead, status_code=status.HTTP_201_CREATED)
def create_link(payload: BookingRequestClientInfoCreate, db: Session = Depends(db_session)):
    return BookingRequestClientInfoService(db).create_link(payload)


@router.get("/{link_id}", response_model=BookingRequestClientInfoRead)
def get_link(link_id: int, db: Session = Depends(db_session)):
    link = BookingRequestClientInfoService(db).get_link(link_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.get("/by-ids/{booking_request_id}/{client_info_id}", response_model=BookingRequestClientInfoRead)
def get_link_by_ids(booking_request_id: int, client_info_id: int, db: Session = Depends(db_session)):
    link = BookingRequestClientInfoService(db).get_by_ids(booking_request_id, client_info_id)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@router.delete("/{link_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(link_id: int, db: Session = Depends(db_session)):
    ok = BookingRequestClientInfoService(db).delete_link(link_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Link not found")
    return None
