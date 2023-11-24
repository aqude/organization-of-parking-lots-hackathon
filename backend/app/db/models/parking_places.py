from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT, INTEGER, TIMESTAMP, FLOAT

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

    parking_longitude = Column(
        'parking_longitude',
        FLOAT,
        nullable=False
    )

    parking_latitude = Column(
        'parking_latitude',
        FLOAT,
        nullable=False
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

    price_for_hour = Column(
        "price_for_hour",
        INTEGER,
        nullable=False
    )

    type_of_parking = Column(
        'type_of_parking',
        TEXT,
        nullable=False
    )
