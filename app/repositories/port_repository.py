from sqlalchemy.orm import Session
from app.models.port import Port
from typing import List, Optional

class PortRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Port:
        obj = Port(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self, search: Optional[str] = None) -> List[Port]:
        query = self.db.query(Port)
        if search:
            query = query.filter(Port.name.ilike(f"%{search}%"))
        return query.order_by(Port.id.desc()).all()

    def get_by_name(self, name: str) -> Optional[Port]:
        return self.db.query(Port).filter(Port.name == name).first()
