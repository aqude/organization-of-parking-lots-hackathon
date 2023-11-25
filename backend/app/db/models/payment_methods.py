from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.models.base import BaseTable


class PaymentMethod(BaseTable):
    __tablename__ = "payment_method"

    type = Column(String, nullable=False, doc="Payment method type.")
    method_id = Column(UUID(as_uuid=True), nullable=False, doc="Payment method ID.")
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user.",
    )
    title = Column(
        String(100),
        index=True,
        unique=True,
        nullable=False,
        doc="Payment method title.",
    )