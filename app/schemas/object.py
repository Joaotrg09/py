from uuid import UUID, uuid4
from pydantic import BaseModel, Field


class ObjectShow(BaseModel):
    id: str = Field(..., alias="_id")
    user_uuid_fk: str
    Name: str | None = None
    Type: str | None = None
    Query: dict | None = None


class Object(BaseModel):
    user_uuid_fk: str
    Name: str | None = None
    Type: str | None = None
    Query: dict | None = None
