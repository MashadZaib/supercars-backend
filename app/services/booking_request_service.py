from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.booking_request import BookingRequest
from app.repositories.booking_request_repository import BookingRequestRepository
from app.schemas.booking_request_schema import BookingRequestCreate, BookingRequestUpdate

class BookingRequestService:
    def __init__(self, db: Session):
        self.repo = BookingRequestRepository(db)

    def create_booking(self, payload: BookingRequestCreate) -> BookingRequest:
        obj = BookingRequest(**payload.dict())
        return self.repo.create(obj)

    def list_bookings(self) -> List[BookingRequest]:
        return self.repo.list()

    def get_booking(self, booking_id: int) -> Optional[BookingRequest]:
        return self.repo.get(booking_id)

    def update_booking(self, booking_id: int, payload: BookingRequestUpdate) -> Optional[BookingRequest]:
        obj = self.repo.get(booking_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_booking(self, booking_id: int) -> bool:
        obj = self.repo.get(booking_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
