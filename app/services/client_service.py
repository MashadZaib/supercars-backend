from typing import List, Optional
from sqlalchemy.orm import Session
from app.schemas.client_schema import ClientCreate, ClientUpdate
from app.models.client import Client
from app.repositories.client_repository import ClientRepository

class ClientService:
    def __init__(self, db: Session):
        self.repo = ClientRepository(db)

    def create_client(self, payload: ClientCreate) -> Client:
        obj = Client(**payload.dict())
        return self.repo.create(obj)

    def list_clients(self) -> List[Client]:
        return self.repo.list()

    def get_client(self, client_id: int) -> Optional[Client]:
        return self.repo.get(client_id)

    def update_client(self, client_id: int, payload: ClientUpdate) -> Optional[Client]:
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
