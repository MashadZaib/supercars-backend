from fastapi import HTTPException, status
from app.repositories.port_repository import RequestTypeRepository
from app.schemas.request_type import RequestTypeCreate

class RequestTypeService:
    def __init__(self, db):
        self.repo = RequestTypeRepository(db)

    def create_request_type(self, payload: RequestTypeCreate):
        existing = self.repo.get_by_name(payload.name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Booking Party already exists"
            )
        return self.repo.create(payload.dict())

    def get_request_types(self, search: str = None):
        return self.repo.get_all(search)
