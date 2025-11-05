from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.booking_confirmation import BookingConfirmation
from app.repositories.booking_confirmation_repository import BookingConfirmationRepository
from app.schemas.booking_confirmation_schema import BookingConfirmationCreate, BookingConfirmationUpdate

class BookingConfirmationService:
    def __init__(self, db: Session):
        self.repo = BookingConfirmationRepository(db)

    def create_confirmation(self, payload: BookingConfirmationCreate) -> BookingConfirmation:
        obj = BookingConfirmation(**payload.dict())
        return self.repo.create(obj)

    def list_by_booking(self, booking_request_id: int) -> List[BookingConfirmation]:
        return self.repo.list_by_booking(booking_request_id)

    def get_confirmation(self, confirmation_id: int) -> Optional[BookingConfirmation]:
        return self.repo.get(confirmation_id)

    def update_confirmation(self, confirmation_id: int, payload: BookingConfirmationUpdate) -> Optional[BookingConfirmation]:
        obj = self.repo.get(confirmation_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_confirmation(self, confirmation_id: int) -> bool:
        obj = self.repo.get(confirmation_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
