from app.schemas.reviews import ReviewIn
from app.db.models import User, Review, Places
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
import uuid

async def create_review(data: ReviewIn, user: User, db: Session):
    parking = db.query(Places).filter(Places.id == data.parking_id).first()
    if not parking:
        return HTTPException(status_code=HTTP_404_NOT_FOUND)
    new_review = Review(parking_id=data.parking_id, user_id=user.id, text=data.text)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


async def get_reviews(parking_id: uuid.UUID, db: Session):
    return db.query(Review).filter(Review.parking_id == parking_id).all()