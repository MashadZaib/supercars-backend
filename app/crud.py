from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from typing import List
import uuid

# Use sha256_crypt to avoid native bcrypt build/runtime issues in some dev
# environments. In production you can switch back to bcrypt if desired.
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_booking(db: Session, booking: schemas.BookingCreate):
    data = booking.dict(exclude_unset=True)
    if not data.get("external_id"):
        data["external_id"] = uuid.uuid4().hex
    db_obj = models.Booking(**data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()


def get_booking_by_external_id(db: Session, external_id: str):
    return db.query(models.Booking).filter(models.Booking.external_id == external_id).first()


def get_bookings(db: Session, skip: int = 0, limit: int = 100) -> List[models.Booking]:
    return db.query(models.Booking).offset(skip).limit(limit).all()


def update_booking(db: Session, booking_id: int, booking: schemas.BookingUpdate):
    db_obj = get_booking(db, booking_id)
    if not db_obj:
        return None
    updates = booking.dict(exclude_unset=True)
    for k, v in updates.items():
        if hasattr(db_obj, k):
            setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_booking_by_external_id(db: Session, external_id: str, booking: schemas.BookingUpdate):
    db_obj = get_booking_by_external_id(db, external_id)
    if not db_obj:
        return None
    updates = booking.dict(exclude_unset=True)
    for k, v in updates.items():
        if hasattr(db_obj, k):
            setattr(db_obj, k, v)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_booking(db: Session, booking_id: int) -> bool:
    db_obj = get_booking(db, booking_id)
    if not db_obj:
        return False
    db.delete(db_obj)
    db.commit()
    return True


def delete_booking_by_external_id(db: Session, external_id: str) -> bool:
    db_obj = get_booking_by_external_id(db, external_id)
    if not db_obj:
        return False
    db.delete(db_obj)
    db.commit()
    return True
