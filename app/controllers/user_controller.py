from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta, datetime
from jose import JWTError, jwt

from app import models, schemas

from sqlalchemy.orm import Session

SECRET_KEY = "chave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "usuario": {
        "username": "usuario",
        "password": "senha123",
    }
}


def login(form_data: OAuth2PasswordRequestForm):
    user = fake_users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": form_data.username, "exp": expire}
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}


def create_user(
    user: schemas.UserRequest, db: Session, current_user: schemas.UserLogin
):
    user_create = models.User(name=user.name, email=user.email)
    db.add(user_create)
    db.commit()
    db.refresh(user_create)

    return user_create


def get_users(db: Session, current_user: schemas.UserLogin):
    users = db.query(models.User).all()
    return users
