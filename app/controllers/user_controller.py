from app import models, schemas

from sqlalchemy.orm import Session


def create_user(user: schemas.UserRequest, db: Session):
    user_create = models.User(name=user.name, email=user.email)
    db.add(user_create)
    db.commit()
    db.refresh(user_create)

    return user_create


def get_users(db: Session):
    users = db.query(models.User).all()
    return users
