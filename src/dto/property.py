from pydantic import BaseModel

from dto.user import User


class Property(BaseModel):
    points: int
    health: int
    energy: int
    ammunition: int

    user_id: int

    class Config:
        orm_mode = True
