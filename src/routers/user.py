from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user as UserService
from dto import user as UserDTO


router = APIRouter()

@router.post('/', tags=['User'])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data=data, db=db)

@router.get('/{user_id}', tags=['User'])
async def get(db: Session = Depends(get_db), user_id: int = None):
    return UserService.get_user(db=db, user_id=user_id)

@router.put('/{user_id}', tags=['User'])
async def update(data: UserDTO.User = None, db: Session = Depends(get_db), user_id: int = None):
    return UserService.update_user(data=data, db=db, user_id=user_id)

@router.delete('/{user_id}', tags=['User'])
async def delete(db: Session = Depends(get_db), user_id: int = None):
    return UserService.delete_user(db=db, user_id=user_id)
