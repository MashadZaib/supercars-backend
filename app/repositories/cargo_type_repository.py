from sqlalchemy.orm import Session
from app.models.cargo_type import CargoType
from typing import List, Optional

class CargoTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> CargoType:
        obj = CargoType(**data)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(self, search: Optional[str] = None) -> List[CargoType]:
        query = self.db.query(CargoType)
        if search:
            query = query.filter(CargoType.name.ilike(f"%{search}%"))
        return query.order_by(CargoType.id.desc()).all()

    def get_by_name(self, name: str) -> Optional[CargoType]:
        return self.db.query(CargoType).filter(CargoType.name == name).first()
