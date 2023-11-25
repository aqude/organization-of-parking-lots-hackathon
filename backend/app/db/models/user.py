from sqlalchemy import Column, DECIMAL
from sqlalchemy.dialects.postgresql import TEXT

from .base import BaseTable


class User(BaseTable):
    __tablename__ = "user"

    email = Column(
        "email",
        TEXT,
        nullable=False,
        unique=True,
        index=True,
        doc="Email.",
    )
    password = Column(
        "password",
        TEXT,
        nullable=False,
        index=True,
        doc="Hashed password.",
    )

    first_name = Column(
        "first_name",
        TEXT,
        nullable=True,
        doc="User first name.",
    )
    last_name = Column(
        "last_name",
        TEXT,
        nullable=True,
        doc="User last name.",
    )