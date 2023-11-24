from pydantic import BaseModel
from typing import Literal


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