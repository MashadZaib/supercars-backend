from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.booking_confirmation import BookingConfirmation

class BookingConfirmationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: BookingConfirmation) -> BookingConfirmation:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[BookingConfirmation]:
        return self.db.query(BookingConfirmation).order_by(BookingConfirmation.id.desc()).all()

    def get(self, booking_id: int) -> Optional[BookingConfirmation]:
        return self.db.query(BookingConfirmation).filter(BookingConfirmation.id == booking_id).first()

    def update(self, db_obj: BookingConfirmation, **changes) -> BookingConfirmation:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: BookingConfirmation) -> None:
        self.db.delete(db_obj)
        self.db.commit()
