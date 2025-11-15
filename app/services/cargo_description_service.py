from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.cargo_description import CargoDescription
from app.repositories.cargo_description_repository import CargoDescriptionRepository
from app.schemas.cargo_description_schema import CargoDescriptionCreate, CargoDescriptionUpdate


class CargoDescriptionService:
    def __init__(self, db: Session):
        self.repo = CargoDescriptionRepository(db)

    def create_description(self, payload: CargoDescriptionCreate) -> CargoDescription:
        obj = CargoDescription(**payload.dict())
        return self.repo.create(obj)

    def list_descriptions(self) -> List[CargoDescription]:
        return self.repo.list()

    def get_description(self, cargo_id: int) -> Optional[CargoDescription]:
        return self.repo.get(cargo_id)

    def update_description(self, cargo_id: int, payload: CargoDescriptionUpdate) -> Optional[CargoDescription]:
        obj = self.repo.get(cargo_id)
        if not obj:
            return None
        return self.repo.update(obj, **payload.dict(exclude_unset=True))

    def delete_description(self, cargo_id: int) -> bool:
        obj = self.repo.get(cargo_id)
        if not obj:
            return False
        self.repo.delete(obj)
        return True
