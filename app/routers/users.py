from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models
from app.controllers import user_controller
from app.db import get_db


router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):
    return user_controller.create_user(user, db)


@router.get("", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)
