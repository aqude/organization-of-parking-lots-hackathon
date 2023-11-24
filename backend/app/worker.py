from app.config import get_settings
from yookassa import Payment, Configuration
from app.db.connection.session import get_sync_session
from app.db.models.payments import Payments as DBPayment
from app.db.models.user import User
from app.config import get_settings
from celery import shared_task

from celery import Celery
from celery.schedules import crontab

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
def confirm_payments():
    session = get_sync_session()

    payments: list[DBPayment] = (
        session.query(DBPayment).filter(DBPayment.status == "pending").all()
    )

    for payment in payments:
        payment_info = Payment.find_one(str(payment.payment_id))
        if payment_info.status == "succeeded":
            payment.is_confirmed = True
        payment.status = payment_info.status
        payment.is_paid = payment_info.paid
    session.commit()
