from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.user_schema import UserCreate, UserRead, UserUpdate
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(db_session)):
    return UserService(db).create_user(payload)

@router.get("/", response_model=List[UserRead])
def list_users(db: Session = Depends(db_session)):
    return UserService(db).list_users()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(db_session)):
    user = UserService(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(db_session)):
    updated = UserService(db).update_user(user_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(db_session)):
    ok = UserService(db).delete_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")
    return None
