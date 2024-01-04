from pydantic import (
    BaseModel, 
    Field, 
    field_validator
)


class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)

    @field_validator('username')
    @classmethod
    def verify_username(cls, value: str) -> None:
        if not value.isalnum():
            raise ValueError('Username contains illegal characters.')
         
        return value.lower()
