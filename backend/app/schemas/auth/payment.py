import uuid
from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime


class PaymentMethodIn(BaseModel):
    type: Literal[
        "bank_card",
        "yoo_money",
        "qiwi",
        "sberbank",
        "tinkoff_bank",
        "sbp",
        "installments",
        "sber_loan",
        "b2b_sberbank",
        "mobile_balance",
        "cash",
    ]


class PaymentMethodOut(BaseModel):
    id: uuid.UUID
    type: Literal[
        "bank_card",
        "yoo_money",
        "qiwi",
        "sberbank",
        "tinkoff_bank",
        "sbp",
        "installments",
        "sber_loan",
        "b2b_sberbank",
        "mobile_balance",
        "cash",
    ]
    title: str


class PaymentOut(BaseModel):
    id: uuid.UUID
    dt_created: datetime
    status: str
    amount: float
    description: Optional[str] = None
    is_confirmed: bool