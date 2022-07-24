import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects import postgresql

from .base import Base


class Team(Base):
    __tablename__ = "teams"

    uid = Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
    name = Column(String)
