from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.client import Client

class ClientInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: Client) -> Client:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[Client]:
        return self.db.query(Client).order_by(Client.id.desc()).all()

    def get(self, client_id: int) -> Optional[Client]:
        return self.db.query(Client).filter(Client.id == client_id).first()

    def update(self, db_obj: Client, **changes) -> Client:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: Client) -> None:
        self.db.delete(db_obj)
        self.db.commit()
