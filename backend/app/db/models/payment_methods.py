from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.models.base import BaseTable


class PaymentMethod(BaseTable):
    __tablename__ = "payment_method"
    method_id = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        doc="Unique index of element (type UUID)",
    )

    type = Column(String, nullable=False, doc="Payment method type.")

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user.",
        primary_key=True
    )
    title = Column(
        String(100),
        index=True,
        unique=True,
        nullable=False,
        doc="Payment method title.",
    )