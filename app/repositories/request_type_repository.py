from sqlalchemy.orm import Session
from app.models.request_type import RequestType
from typing import List, Optional

class RequestTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> RequestType:
        obj = RequestType(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self, search: Optional[str] = None) -> List[RequestType]:
        query = self.db.query(RequestType)
        if search:
            query = query.filter(RequestType.name.ilike(f"%{search}%"))
        return query.order_by(RequestType.id.desc()).all()

    def get_by_name(self, name: str) -> Optional[RequestType]:
        return self.db.query(RequestType).filter(RequestType.name == name).first()
