from datetime import datetime, timedelta
import uuid
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from app.config.utils import get_settings
from app.db.models.parking_places import Places
from app.db.models.payment_methods import PaymentMethod
from app.db.models.reservations import Reservations
from app.db.models.user import User
from yookassa import Payment, Configuration
from app.schemas.reservations import ReservationIn, ReservationDelete
import math
from app.db.models import Payments as DBPayment
import pytz


Configuration.account_id = get_settings().YOOKASSA_ACCOUNT_ID
Configuration.secret_key = get_settings().YOOKASSA_SECRET_KEY


async def create_reservation(data: ReservationIn, user: User, db: Session):
    place: Places = db.query(Places).filter(Places.id == data.parking_id).first()
    if not place:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Place not found")
    if place.number_of_places == 0:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Parking is full")
    payment_method: PaymentMethod = (
        db.query(PaymentMethod)
        .filter(PaymentMethod.id == data.payment_method_id)
        .first()
    )
    if not payment_method:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Payment method not found"
        )
    end_time = (datetime.now(tz=pytz.UTC) + timedelta(days=1)).replace(
        hour=0, minute=0, second=0
    )
    reservation = Reservations(
        parking_id=place.id,
        user_id=user.id,
        payment_method_id=payment_method.id,
        start_time=datetime.now(tz=pytz.UTC),
        end_time=end_time,
    )
    db.add(reservation)
    place.number_of_places -= 1
    db.commit()
    db.refresh(reservation)
    return reservation


async def delete_reservation(data: ReservationDelete, user: User, db: Session):
    reservation: Reservations = (
        db.query(Reservations).filter(Reservations.id == data.id).first()
    )
    if not reservation:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Reservation not found"
        )
    amount = reservation.parking.price * (
        math.ceil((datetime.now() - reservation.start_time).seconds / 3600)
    )

    return_id = uuid.uuid4()
    new_payment = DBPayment(user_id=user.id, id=return_id, amount=amount)
    method: PaymentMethod = (
        db.query(PaymentMethod)
        .filter(PaymentMethod.id == reservation.payment_method_id)
        .first()
    )
    if not method:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="Payment method not found"
        )
    payment = Payment.create(
        {
            "amount": {
                "value": amount,
                "currency": "RUB",
            },
            "capture": True,
            "payment_method_id": method.method_id,
        }
    )
    new_payment.payment_id = payment.id
    new_payment.is_paid = payment.paid
    new_payment.status = payment.status
    db.add(new_payment)
    reservation.parking.number_of_places += 1
    db.delete(reservation)
    db.commit()


async def get_reservations(user: User, db: Session):
    return db.query(Reservations).filter(Reservations.user_id == user.id).all()