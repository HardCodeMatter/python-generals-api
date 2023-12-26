from pydantic import BaseModel

from dto.user import User


class Property(BaseModel):
    points: int
    health: int
    energy: int
    ammunition: int

    user_id: User | None

    class Config:
        orm_mode = True
