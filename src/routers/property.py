from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import property as PropertyService
from dto import property as PropertyDTO


router = APIRouter()

@router.post('/', tags=['Property'])
async def create(data: PropertyDTO.Property = None, db: Session = Depends(get_db)):
    return PropertyService.create_property(data=data, db=db)

@router.get('/{property_id}', tags=['Property'])
async def get(db: Session = Depends(get_db), property_id: int = None):
    return PropertyService.get_property(db=db, property_id=property_id)

@router.put('/{property_id}', tags=['Property'])
async def update(data: PropertyDTO.Property = None, db: Session = Depends(get_db), property_id: int = None):
    return PropertyService.update_property(data=data, db=db, property_id=property_id)

@router.delete('/{property_id}', tags=['Property'])
async def delete(db: Session = Depends(get_db), property_id: int = None):
    return PropertyService.delete_property(db=db, property_id=property_id)
