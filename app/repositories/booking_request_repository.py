from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.booking_request import BookingRequest

class BookingRequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: BookingRequest) -> BookingRequest:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[BookingRequest]:
        return self.db.query(BookingRequest).order_by(BookingRequest.id.desc()).all()

    def get(self, booking_id: int) -> Optional[BookingRequest]:
        return self.db.query(BookingRequest).filter(BookingRequest.id == booking_id).first()

    def update(self, db_obj: BookingRequest, **changes) -> BookingRequest:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: BookingRequest) -> None:
        self.db.delete(db_obj)
        self.db.commit()
