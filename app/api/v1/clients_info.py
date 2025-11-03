from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.client_info_schema import (
    ClientInfoCreate,
    ClientInfoRead,
    ClientInfoUpdate
)
from app.services.client_info_service import ClientInfoService

router = APIRouter()

@router.post("/", response_model=ClientInfoRead, status_code=status.HTTP_201_CREATED)
def create_client(payload: ClientInfoCreate, db: Session = Depends(db_session)):
    return ClientInfoService(db).create_client(payload)

@router.get("/", response_model=List[ClientInfoRead])
def list_clients(db: Session = Depends(db_session)):
    return ClientInfoService(db).list_clients()

@router.get("/{client_id}", response_model=ClientInfoRead)
def get_client(client_id: int, db: Session = Depends(db_session)):
    client = ClientInfoService(db).get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientInfoRead)
def update_client(client_id: int, payload: ClientInfoUpdate, db: Session = Depends(db_session)):
    updated = ClientInfoService(db).update_client(client_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Client not found")
    return updated

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(db_session)):
    ok = ClientInfoService(db).delete_client(client_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Client not found")
    return None
