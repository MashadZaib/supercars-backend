from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.core.dependencies import db_session
from app.schemas.client_schema import ClientCreate, ClientRead, ClientUpdate
from app.services.client_service import ClientService

router = APIRouter()

@router.post("/", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
def create_client(payload: ClientCreate, db: Session = Depends(db_session)):
    return ClientService(db).create_client(payload)

@router.get("/", response_model=List[ClientRead])
def list_clients(db: Session = Depends(db_session)):
    return ClientService(db).list_clients()

@router.get("/{client_id}", response_model=ClientRead)
def get_client(client_id: int, db: Session = Depends(db_session)):
    client = ClientService(db).get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientRead)
def update_client(client_id: int, payload: ClientUpdate, db: Session = Depends(db_session)):
    client = ClientService(db).update_client(client_id, payload)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(db_session)):
    ok = ClientService(db).delete_client(client_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Client not found")
    return None
