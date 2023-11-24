from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.models.base import BaseTable


class PaymentMethod(BaseTable):
    __tablename__ = "payment_method"

    type = Column(String, nullable=False, doc="Payment method type.")
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        doc="ID of user.",
    )
    title = Column(String(100))