from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Security


from app import schemas, models
from app.controllers import user_controller
from app.db import get_db
from app.auth import get_current_user

security = HTTPBearer()


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(security)],
)


@router.post(
    "",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Security(security)],
)
def create_user(
    user: schemas.UserRequest,
    db: Session = Depends(get_db),
    current_user: schemas.UserLogin = Depends(get_current_user),
):
    return user_controller.create_user(user, db)


@router.get(
    "",
    response_model=List[schemas.UserResponse],
    dependencies=[Security(security)],
)
def get_users(
    db: Session = Depends(get_db),
    current_user: schemas.UserLogin = Depends(get_current_user),
):
    return user_controller.get_users(db)
