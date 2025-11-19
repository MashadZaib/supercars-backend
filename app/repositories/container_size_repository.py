from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.container_size import ContainerSize


class ContainerSizeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: ContainerSize) -> ContainerSize:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> List[ContainerSize]:
        return self.db.query(ContainerSize).order_by(ContainerSize.id.desc()).all()

    def get(self, size_id: int) -> Optional[ContainerSize]:
        return self.db.query(ContainerSize).filter(ContainerSize.id == size_id).first()

    def update(self, db_obj: ContainerSize, **changes) -> ContainerSize:
        for k, v in changes.items():
            setattr(db_obj, k, v)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: ContainerSize) -> None:
        self.db.delete(db_obj)
        self.db.commit()
