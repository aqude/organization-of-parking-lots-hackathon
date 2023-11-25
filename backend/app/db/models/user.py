from sqlalchemy import Column, DECIMAL
from sqlalchemy.dialects.postgresql import TEXT

from .base import BaseTable


class User(BaseTable):
    __tablename__ = "user"

    first_name = Column(
        "first_name",
        TEXT,
        nullable=False,
        unique=False,
        index=True,
        doc="first_name for registration.",
    )

    second_name = Column(
        "second_name",
        TEXT,
        nullable=False,
        unique=False,
        index=True,
        doc="second_name for registration.",
    )

    last_name = Column(
        "last_name",
        TEXT,
        nullable=True,
        unique=False,
        index=True,
        doc="last_name for registration.",
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
