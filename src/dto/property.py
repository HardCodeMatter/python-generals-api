from pydantic import BaseModel, Field


class Property(BaseModel):
    points: int = Field(default=5)
    health: int = Field(default=100)
    energy: int = Field(default=100)
    ammunition: int = Field(default=5)

    user_id: int

    class Config:
        orm_mode = True
