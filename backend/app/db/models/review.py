from sqlalchemy import Column, ForeignKey, String, DECIMAL, BOOLEAN, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db import DeclarativeBase
from .base import BaseTable


class Review(DeclarativeBase):
    __tablename__ = "reviews"

    dt_created = Column(
        TIMESTAMP(timezone=True),
        server_default=func.current_timestamp(),
        nullable=False,
        doc="Date and time of create (type TIMESTAMP)",
    ) 
    parking_id = Column(UUID(as_uuid=True), ForeignKey("Places.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    text = Column(String, nullable=False)
    