from sqlalchemy import INTEGER, TIMESTAMP, ForeignKey, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.models.base import BaseTable


class Reservations(BaseTable):
    __tablename__ = "reservations"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user.",
    )
    user = relationship("User")
    parking_id = Column(
        UUID(as_uuid=True),
        ForeignKey("Places.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of place.",
    )
    parking = relationship("Places", back_populates="reservations")
    payment_method_id = Column(
        UUID(as_uuid=True),
        ForeignKey("payment_method.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of payment method.",
    )
    payment_method = relationship("PaymentMethod")
    start_time = Column(
        TIMESTAMP,
        nullable=False,
        doc="Start time of reservation.",
    )
    end_time = Column(
        TIMESTAMP,
        nullable=False,
        doc="End time of reservation.",
    )