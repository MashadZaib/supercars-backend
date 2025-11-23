from pydantic import BaseModel
from app.models.enums import MethodEnum
from datetime import date

class BookingRequestClientInfoBase(BaseModel):
    booking_request_id: int
    client_info_id: int
    method_type: MethodEnum
    entry_date: date

class BookingRequestClientInfoCreate(BookingRequestClientInfoBase):
    pass


class BookingRequestClientInfoRead(BookingRequestClientInfoBase):
    id: int

    class Config:
        from_attributes = True
