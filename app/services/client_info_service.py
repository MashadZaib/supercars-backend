from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.client_info import ClientInfo
from app.repositories.client_info_repository import ClientInfoRepository
from app.schemas.client_info_schema import ClientInfoCreate, ClientInfoUpdate

class ClientInfoService:
    def __init__(self, db: Session):
        self.repo = ClientInfoRepository(db)

    def create_client(self, payload: ClientInfoCreate) -> ClientInfo:
        obj = ClientInfo(**payload.dict())
        return self.repo.create(obj)

    def list_clients(self) -> List[ClientInfo]:
        return self.repo.list()

    def get_client(self, client_id: int) -> Optional[ClientInfo]:
        return self.repo.get(client_id)

    def update_client(self, client_id: int, payload: ClientInfoUpdate) -> Optional[ClientInfo]:
        obj = self.repo.get(client_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_client(self, client_id: int) -> bool:
        obj = self.repo.get(client_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
