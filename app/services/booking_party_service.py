from fastapi import HTTPException, status
from app.repositories.booking_party_repository import BookingPartyRepository
from app.schemas.booking_party_schema import BookingPartyCreate

class BookingPartyService:
    def __init__(self, db):
        self.repo = BookingPartyRepository(db)

    def create_booking_party(self, payload: BookingPartyCreate):
        existing = self.repo.get_by_name(payload.name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Booking Party already exists"
            )
        return self.repo.create(payload.dict())

    def get_booking_parties(self, search: str = None):
        return self.repo.get_all(search)
