from sqlalchemy import Column, ForeignKey, String, DECIMAL, BOOLEAN
from sqlalchemy.dialects.postgresql import UUID

from .base import BaseTable


class Payments(BaseTable):
    __tablename__ = "payment"

    user_id = Column(
        "user_id",
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user",
    )

    payment_id = Column(
        UUID(as_uuid=True),
        index=True,
        nullable=True,
        unique=True,
        doc="YooKassa payment ID.",
    )

    status = Column(String, nullable=False, doc="Payment status.")

    amount = Column(DECIMAL, nullable=False, doc="Payment amount.")

    description = Column(String, nullable=False, doc="Payment description.")

    is_paid = Column(BOOLEAN, default=False, doc="YooKassa paid status.")

    is_confirmed = Column(
        BOOLEAN, default=False, doc="YooKassa status of confirmation."
    )