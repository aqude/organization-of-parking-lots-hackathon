from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT, INTEGER
from app.db import DeclarativeBase


class Cities(DeclarativeBase):
    __tablename__ = "Cities"

    name = Column(
        'city_name',
        TEXT,
        nullable=False,
        primary_key=True,
        unique=True
    )

    id = Column(
        'city_id',
        INTEGER,
        primary_key=True,
        nullable=False,
        unique=True
    )
