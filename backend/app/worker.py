from datetime import datetime, timedelta
import math
from app.config import get_settings
from yookassa import Payment, Configuration
from app.db.connection.session import get_sync_session
from app.db.models.parking_places import Places
from app.db.models.payments import Payments as DBPayment
from app.db.models.reservations import Reservations
from app.db.models.user import User
from app.config import get_settings
from celery import shared_task
from app.utils.get_places.get_place import get_place_by_id
from app.utils.payment import create_payment

from celery import Celery
from celery.schedules import crontab

from app.utils.user.business_logic import get_user_by_id

celery_app = Celery(
    __name__,
    broker=get_settings().CELERY_BROKER_URL,
    backend=get_settings().CELERY_RESULT_BACKEND,
)

celery_app.conf.beat_schedule = {
    "confirm_payments": {
        "task": "app.worker.confirm_payments",
        "schedule": crontab(minute="*/1"),
    },
}

celery_app.autodiscover_tasks()
Configuration.account_id = get_settings().YOOKASSA_ACCOUNT_ID
Configuration.secret_key = get_settings().YOOKASSA_SECRET_KEY


@celery_app.task
def check_reservations():
    session = get_sync_session()

    reservations: list[Reservations] = (
        session.query(Reservations)
        .filter(
            Reservations.occupied_to <= datetime.now(),
            Reservations.occupied_to >= datetime.now() + timedelta(minutes=1),
        )
        .all()
    )

    for reservation in reservations:
        payment = (
            session.query(DBPayment)
            .filter(DBPayment.id == reservation.payment_id)
            .first()
        )
        if payment and payment.is_confirmed:
            continue
        place: Places = get_place_by_id(session, reservation.place_id)
        amount = place.price_for_hour * (
            math.ceil(
                (reservation.occupied_to - reservation.occupied_from).seconds / 3600
            )
        )
        user = get_user_by_id(session, reservation.user_id)
        if not user:
            continue

        session, payment = create_payment(session, reservation, user, amount)
        if payment.status == "succeeded" or payment.status == "pending":
            payment.is_confirmed = True
            place.status = True
            session.delete(reservation)
            session.commit()