from sqlalchemy import Column, ForeignKey, DECIMAL
from sqlalchemy.dialects.postgresql import TEXT, INTEGER
from sqlalchemy.orm import relationship

from app.db.models.base import BaseTable


class Places(BaseTable):
    __tablename__ = "Places"

    City_id = Column("City_id", ForeignKey("Cities.city_id"), nullable=False)
    parking_longitude = Column("parking_longitude", DECIMAL, index=True, nullable=False)
    parking_latitude = Column("parking_latitude", DECIMAL, index=True, nullable=False)
    number_of_places = Column("number_of_places", INTEGER, nullable=False)
    price = Column("price", DECIMAL, nullable=False)
    description = Column("description", TEXT, nullable=True)
    reservations = relationship("Reservations", back_populates="parking")
    street_name = Column("street_name", TEXT, nullable=True)