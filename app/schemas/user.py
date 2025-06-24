from uuid import UUID

from pydantic import BaseModel


class UserLogin(BaseModel):
    username: str
    password: str


class UserRequest(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str

    class config:
        orm_mode = True
