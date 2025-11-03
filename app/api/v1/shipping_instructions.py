from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import db_session
from app.schemas.shipping_instruction_schema import (
    ShippingInstructionCreate,
    ShippingInstructionRead,
    ShippingInstructionUpdate,
)
from app.services.shipping_instruction_service import ShippingInstructionService

router = APIRouter()

@router.post("/", response_model=ShippingInstructionRead, status_code=status.HTTP_201_CREATED)
def create_instruction(payload: ShippingInstructionCreate, db: Session = Depends(db_session)):
    return ShippingInstructionService(db).create_instruction(payload)

@router.get("/", response_model=List[ShippingInstructionRead])
def list_instructions(db: Session = Depends(db_session)):
    return ShippingInstructionService(db).list_instructions()

@router.get("/{instruction_id}", response_model=ShippingInstructionRead)
def get_instruction(instruction_id: int, db: Session = Depends(db_session)):
    instruction = ShippingInstructionService(db).get_instruction(instruction_id)
    if not instruction:
        raise HTTPException(status_code=404, detail="Shipping instruction not found")
    return instruction

@router.put("/{instruction_id}", response_model=ShippingInstructionRead)
def update_instruction(instruction_id: int, payload: ShippingInstructionUpdate, db: Session = Depends(db_session)):
    updated = ShippingInstructionService(db).update_instruction(instruction_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Shipping instruction not found")
    return updated

@router.delete("/{instruction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instruction(instruction_id: int, db: Session = Depends(db_session)):
    ok = ShippingInstructionService(db).delete_instruction(instruction_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Shipping instruction not found")
    return None
