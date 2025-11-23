from typing import Optional
from sqlalchemy.orm import Session

from app.models.booking_request_client_info import BookingRequestClientInfo
from app.repositories.booking_request_client_info_repository import (
    BookingRequestClientInfoRepository
)
from app.schemas.booking_request_client_info_schema import (
    BookingRequestClientInfoCreate
)


class BookingRequestClientInfoService:
    def __init__(self, db: Session):
        self.repo = BookingRequestClientInfoRepository(db)

    def create_link(self, payload: BookingRequestClientInfoCreate) -> BookingRequestClientInfo:
        data = payload.dict(exclude_unset=True)
        obj = BookingRequestClientInfo(**data)
        return self.repo.create(obj)

    def get_link(self, link_id: int) -> Optional[BookingRequestClientInfo]:
        return self.repo.get(link_id)

    def get_by_ids(self, booking_request_id: int, client_info_id: int) -> Optional[BookingRequestClientInfo]:
        return self.repo.get_by_ids(booking_request_id, client_info_id)

    def delete_link(self, link_id: int) -> bool:
        obj = self.repo.get(link_id)
        if not obj:
            return False

        self.repo.delete(obj)
        return True
