from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session

from app import schemas

from typing import List

from app.db import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post(
    "/users", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserRequest, db: Session = Depends(get_db)):

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.get("/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
