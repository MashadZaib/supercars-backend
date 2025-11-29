from sqlalchemy import Column, Integer, String, Enum
import enum
from app.core.database import Base

class RoleEnum(enum.Enum):
    admin = "admin"
    user = "user"
    manager = "manager"
    shipper = "shipper"
    client = "client"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.user)
    address = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    contact_person = Column(String(50), nullable=True)