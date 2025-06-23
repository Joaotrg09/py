import uuid

import sqlalchemy as Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id: Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name: Column(String, nullable=False)
    email: Column(String, nullable=True)
