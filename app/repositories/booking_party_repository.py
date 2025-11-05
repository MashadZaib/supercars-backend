from sqlalchemy.orm import Session
from app.models.booking_party import BookingParty
from typing import List, Optional

class BookingPartyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> BookingParty:
        obj = BookingParty(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self, search: Optional[str] = None) -> List[BookingParty]:
        query = self.db.query(BookingParty)
        if search:
            query = query.filter(BookingParty.name.ilike(f"%{search}%"))
        return query.order_by(BookingParty.id.desc()).all()

    def get_by_name(self, name: str) -> Optional[BookingParty]:
        return self.db.query(BookingParty).filter(BookingParty.name == name).first()
