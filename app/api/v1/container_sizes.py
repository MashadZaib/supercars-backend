from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.container_size_schema import (
    ContainerSizeCreate,
    ContainerSizeRead,
    ContainerSizeUpdate
)
from app.services.container_size_service import ContainerSizeService

router = APIRouter()

@router.post("/", response_model=ContainerSizeRead, status_code=status.HTTP_201_CREATED)
def create_container_size(payload: ContainerSizeCreate, db: Session = Depends(db_session)):
    return ContainerSizeService(db).create_size(payload)

@router.get("/", response_model=List[ContainerSizeRead])
def list_container_sizes(db: Session = Depends(db_session)):
    return ContainerSizeService(db).list_sizes()

@router.get("/{size_id}", response_model=ContainerSizeRead)
def get_container_size(size_id: int, db: Session = Depends(db_session)):
    size = ContainerSizeService(db).get_size(size_id)
    if not size:
        raise HTTPException(status_code=404, detail="Container size not found")
    return size

@router.put("/{size_id}", response_model=ContainerSizeRead)
def update_container_size(size_id: int, payload: ContainerSizeUpdate, db: Session = Depends(db_session)):
    updated = ContainerSizeService(db).update_size(size_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Container size not found")
    return updated

@router.delete("/{size_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_container_size(size_id: int, db: Session = Depends(db_session)):
    ok = ContainerSizeService(db).delete_size(size_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Container size not found")
    return None
