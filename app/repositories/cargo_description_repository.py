from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.cargo_description import CargoDescription


class CargoDescriptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: CargoDescription) -> CargoDescription:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[CargoDescription]:
        return self.db.query(CargoDescription).order_by(CargoDescription.id.desc()).all()

    def get(self, cargo_id: int) -> Optional[CargoDescription]:
        return self.db.query(CargoDescription).filter(CargoDescription.id == cargo_id).first()

    def update(self, db_obj: CargoDescription, **changes) -> CargoDescription:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: CargoDescription) -> None:
        self.db.delete(db_obj)
        self.db.commit()
