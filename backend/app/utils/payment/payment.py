import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from yookassa import Payment, Configuration, Refund

from app.db.models import Payments as DBPayment, User
from app.db.models import PaymentMethod
from app.db.models.parking_places import Places
from app.db.models.reservations import Reservations
from app.schemas.auth.payment import PaymentMethodIn
from app.config import get_settings


Configuration.account_id = get_settings().YOOKASSA_ACCOUNT_ID
Configuration.secret_key = get_settings().YOOKASSA_SECRET_KEY


async def create_payment_method(
    session: AsyncSession, user: User, payment_method: PaymentMethodIn
) -> str:
    return_id = uuid.uuid4()
    new_payment = DBPayment(user_id=user.id, id=return_id, amount=2, description="test")
    return_url = f"http://127.0.0.1:3000/payment_successful?id={return_id}"
    print("test")
    payment = Payment.create(
        {
            "amount": {"value": 2.0, "currency": "RUB"},
            "payment_method_data": {"type": payment_method.type},
            "confirmation": {
                "type": "redirect",
                "return_url": return_url,
            },
            "capture": True,
            "save_payment_method": True,
        }
    )
    print("test1")
    new_payment.payment_id = payment.id
    new_payment.is_paid = payment.paid
    new_payment.status = payment.status
    session.add(new_payment)
    await session.commit()
    return payment.confirmation.confirmation_url


async def confirm_payment(session: AsyncSession, user: User, id: uuid.UUID) -> str:
    query = select(DBPayment).where(DBPayment.id == id)
    payment: DBPayment = await session.scalar(query)
    if payment is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Payment not found")
    if payment.user_id != user.id:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Forbidden")
    payment_info = Payment.find_one(str(payment.payment_id))
    if payment_info.status == "succeeded":
        response = "Payment confirmed"
        user.balance += payment.amount
        payment.is_confirmed = True
        new_payment_method = PaymentMethod(
            user_id=user.id,
            id=payment_info.payment_method.id,
            title=payment_info.payment_method.title,
            type=payment_info.payment_method.type,
        )
        refund = Refund.create(
            {
                "amount": {"value": "2.00", "currency": "RUB"},
                "payment_id": str(payment.payment_id),
            }
        )
        if refund.status == "canceled":
            response = "Refund canceled: " + refund.cancellation_details.reason
        session.add(new_payment_method)
    else:
        response = "Payment is still pending"
    payment.status = payment_info.status
    payment.is_paid = payment_info.paid
    await session.commit()
    return response


def create_payment(
    session: Session, reservation: Reservations, user: User, amount: float
) -> tuple[Session, DBPayment]:
    return_id = uuid.uuid4()
    new_payment = DBPayment(user_id=user.id, id=return_id, amount=amount)
    payment = Payment.create(
        {
            "amount": {
                "value": amount,
                "currency": "RUB",
            },
            "capture": True,
            "payment_method_id": reservation.payment_method_id,
        }
    )
    new_payment.payment_id = payment.id
    new_payment.is_paid = payment.paid
    new_payment.status = payment.status
    session.add(new_payment)
    return session, new_payment