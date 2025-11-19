from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.container_size import ContainerSize
from app.repositories.container_size_repository import ContainerSizeRepository
from app.schemas.container_size_schema import ContainerSizeCreate, ContainerSizeUpdate


class ContainerSizeService:
    def __init__(self, db: Session):
        self.repo = ContainerSizeRepository(db)

    def create_size(self, payload: ContainerSizeCreate) -> ContainerSize:
        obj = ContainerSize(**payload.dict())
        return self.repo.create(obj)

    def list_sizes(self) -> List[ContainerSize]:
        return self.repo.list()

    def get_size(self, size_id: int) -> Optional[ContainerSize]:
        return self.repo.get(size_id)

    def update_size(self, size_id: int, payload: ContainerSizeUpdate) -> Optional[ContainerSize]:
        obj = self.repo.get(size_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_size(self, size_id: int) -> bool:
        obj = self.repo.get(size_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
