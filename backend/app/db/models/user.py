from sqlalchemy import Column, DECIMAL
from sqlalchemy.dialects.postgresql import TEXT

from .base import BaseTable


class User(BaseTable):
    __tablename__ = "user"

    username = Column(
        "username",
        TEXT,
        nullable=False,
        unique=True,
        index=True,
        doc="Username for authentication.",
    )
    password = Column(
        "password",
        TEXT,
        nullable=False,
        index=True,
        doc="Hashed password.",
    )
    email = Column(
        "email",
        TEXT,
        nullable=True,
        unique=True,
        doc="Email for notifications.",
    )

    balance = Column(
        "balance",
        DECIMAL(asdecimal=True),
        default=0.0,
        doc="User balance"
    )
