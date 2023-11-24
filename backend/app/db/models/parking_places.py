from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT, INTEGER, TIMESTAMP
from app.db import DeclarativeBase


class Places(DeclarativeBase):
    __tablename__ = "Places"
    __table_args__ = (
        {
        'postgresql_partition_by': 'LIST ("City_id")',
        }
    )

    City = Column(
        'City',
        TEXT,
        nullable=False,
        primary_key=True
    )

    City_id = Column(
        'City_id',
        ForeignKey("Cities.city_id"),
        nullable=False
    )

    parking_address = Column(
        'parking_address',
        TEXT,
        nullable=False,
    )

    number_of_place = Column(
        'number_of_place',
        INTEGER,
        nullable=False
    )

    time_occupied_from = Column(
        'time_occupied_from',
        TIMESTAMP(timezone=True),
        nullable=True
    )

    time_occupied_to = Column(
        'time_occupied_to',
        TIMESTAMP(timezone=True),
        nullable=True
    )
