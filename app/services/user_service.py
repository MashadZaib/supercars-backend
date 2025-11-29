from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, payload: UserCreate) -> User:
        try:
            hashed_pw = pwd_context.hash(payload.password)
            obj = User(
                username=payload.username,
                email=payload.email,
                password=hashed_pw,
                role=payload.role,
                address=payload.address,
                phone=payload.phone,
                contact_person=payload.contact_person,
            )
            return self.repo.create(obj)

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )

    def list_users(self) -> List[User]:
        return self.repo.list()

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repo.get(user_id)

    def update_user(self, user_id: int, payload: UserUpdate) -> Optional[User]:
        obj = self.repo.get(user_id)
        if not obj:
            return None

        changes = payload.dict(exclude_unset=True)

        if "password" in changes:
            changes["password"] = pwd_context.hash(changes["password"])

        return self.repo.update(obj, **changes)

    def delete_user(self, user_id: int) -> bool:
        obj = self.repo.get(user_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
