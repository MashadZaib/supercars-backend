from sqlalchemy import Enum, Column, Integer, ForeignKey, Date
from app.models.enums import MethodEnum
from app.core.database import Base
import enum
from datetime import date


class BookingRequestClientInfo(Base):
    __tablename__ = "booking_request_client_info"

    id = Column(Integer, primary_key=True, index=True)

    booking_request_id = Column(Integer, ForeignKey("booking_requests.id", ondelete="CASCADE"), nullable=False)
    client_info_id = Column(Integer, ForeignKey("client_info.id", ondelete="CASCADE"), nullable=False)
    entry_date = Column(Date, nullable=False, default=date.today)
    # NEW FIELD
    method_type = Column(
        Enum(MethodEnum, name="methodenum", native_enum=False),
        nullable=False,
        default=MethodEnum.email,
    )
