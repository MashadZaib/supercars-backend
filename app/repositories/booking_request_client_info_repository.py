from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.booking_request_client_info import BookingRequestClientInfo


class BookingRequestClientInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: BookingRequestClientInfo) -> BookingRequestClientInfo:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[BookingRequestClientInfo]:
        return self.db.query(BookingRequestClientInfo).order_by(
            BookingRequestClientInfo.id.desc()
        ).all()

    def get(self, link_id: int) -> Optional[BookingRequestClientInfo]:
        return self.db.query(BookingRequestClientInfo).filter(
            BookingRequestClientInfo.id == link_id
        ).first()

    def get_by_ids(self, booking_request_id: int, client_info_id: int) -> Optional[BookingRequestClientInfo]:
        return self.db.query(BookingRequestClientInfo).filter(
            BookingRequestClientInfo.booking_request_id == booking_request_id,
            BookingRequestClientInfo.client_info_id == client_info_id
        ).first()

    def delete(self, db_obj: BookingRequestClientInfo) -> None:
        self.db.delete(db_obj)
        self.db.commit()
