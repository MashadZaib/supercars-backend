from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.database import get_db
from app.services.request_type_service import RequestTypeService
from app.schemas.request_type import RequestTypeCreate, RequestTypeBase

router = APIRouter()

@router.post("/", response_model=RequestTypeBase)
def create_request_type(payload: RequestTypeCreate, db: Session = Depends(get_db)):
    return RequestTypeService(db).create_request_type(payload)

@router.get("/", response_model=List[RequestTypeBase])
def list_request_types(
    search: Optional[str] = Query(None, description="Search Request Type by name"),
    db: Session = Depends(get_db)
):
    return RequestTypeService(db).get_request_types(search)
