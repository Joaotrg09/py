from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas
from app.controllers import user_controller

router = APIRouter(prefix="/login", tags=["Login"])


@router.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_controller.login(form_data)
