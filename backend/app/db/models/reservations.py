from sqlalchemy import INTEGER, TIMESTAMP, ForeignKey, Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.models.base import BaseTable


class Reservations(BaseTable):
    __tablename__ = "reservations"

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user.",
        unique=True,
    )
    place_id = Column(
        INTEGER,
        nullable=False,
        doc="ID of place.",
        unique=True,
    )
    occupied_from = Column(
        TIMESTAMP,
        nullable=False,
        doc="Start time of reservation.",
    )
    occupied_to = Column(
        TIMESTAMP,
        nullable=False,
        doc="End time of reservation.",
    )
    payment_method_id = Column(
        UUID(as_uuid=True),
        ForeignKey("payment_method.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of payment method.",
    )

    payment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("payment.id", ondelete="CASCADE"),
        nullable=True,
        doc="Payment ID.",
    )