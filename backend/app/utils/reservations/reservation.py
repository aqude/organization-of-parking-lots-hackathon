from datetime import datetime, timedelta
import uuid
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND
from app.config.utils import get_settings
from app.db.models.parking_places import Places
from app.db.models.payment_methods import PaymentMethod
from app.db.models.reservations import Reservations
from app.db.models.user import User
from yookassa import Payment, Configuration
from app.schemas.update_place.update_place import UpdatePlaceReq
from app.utils.payment.payment import create_payment
import math
from app.db.models import Payments as DBPayment


Configuration.account_id = get_settings().YOOKASSA_ACCOUNT_ID
Configuration.secret_key = get_settings().YOOKASSA_SECRET_KEY


async def create_reservation(session: AsyncSession, data: UpdatePlaceReq, user: User):
    query = select(PaymentMethod).where(
        PaymentMethod.title == data.payment_method_title
    )
    payment_method = await session.scalar(query)
    if not payment_method:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Payment method not found"
        )
    next_day_midnight = (datetime.now() + timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    reservation = Reservations(
        place_id=data.number_of_place,
        user_id=user.id,
        payment_method_id=payment_method.id,
        occupied_from=datetime.now(),
        occupied_to=next_day_midnight,
    )

    session.add(reservation)
    await session.commit()
    return reservation


async def delete_reservation(session: AsyncSession, data: Places, user: User):
    query = select(Reservations).where(
        Reservations.user_id == user.id,
        Reservations.place_id == data.number_of_place,
    )
    reservation = await session.scalar(query)
    if not reservation:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Reservation not found"
        )
    amount = data.price_for_hour * (
        math.ceil((datetime.now() - reservation.occupied_from).seconds / 3600)
    )

    return_id = uuid.uuid4()
    new_payment = DBPayment(
        user_id=user.id, id=return_id, amount=amount, description="test"
    )
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
    return session, new_payment, reservation