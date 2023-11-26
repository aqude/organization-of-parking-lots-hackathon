from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from app.db.models import User
from app.db.connection.session import get_sync_session
from app.utils.user.business_logic import get_current_user
from app.utils.reviews import create_review, get_reviews
from app.schemas.reviews import ReviewIn, ReviewOut
import uuid
from app.utils.user import get_user_by_id

router = APIRouter(
    prefix="/reviews",
    tags=["Review"],
)

@router.post("/create", response_model=ReviewOut)
async def create_parking_review(data: ReviewIn, user: User = Depends(get_current_user), session: Session = Depends(get_sync_session)):
    result = await create_review(data, user, session)
    response = ReviewOut(**result.__dict__, user_fullname=user.first_name + " " + user.second_name) 
    return response

@router.get("/list/{parking_id}", response_model=list[ReviewOut])
async def list_parking_reviews(parking_id: uuid.UUID, db: Session = Depends(get_sync_session)):
    reviews = await get_reviews(parking_id, db)
    new_reviews = list()
    for review in reviews:
        user = get_user_by_id(db, review.user_id)
        new_reviews.append(ReviewOut(**review.__dict__, user_fullname=user.first_name + " " + user.second_name))
    return new_reviews