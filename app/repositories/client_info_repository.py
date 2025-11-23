from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.client_info import ClientInfo


class ClientInfoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: ClientInfo) -> ClientInfo:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[ClientInfo]:
        return self.db.query(ClientInfo).order_by(ClientInfo.id.desc()).all()

    def get(self, client_id: int) -> Optional[ClientInfo]:
        return self.db.query(ClientInfo).filter(
            ClientInfo.id == client_id
        ).first()

    def update(self, db_obj: ClientInfo, **changes) -> ClientInfo:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: ClientInfo) -> None:
        self.db.delete(db_obj)
        self.db.commit()
