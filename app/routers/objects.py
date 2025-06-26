from fastapi import APIRouter, Depends
from typing import List
from pymongo.database import Database

from app.controllers import object_controller
from app.db.mongodb import get_mongodb

from app import schemas

from uuid import UUID

router = APIRouter(prefix="/objects", tags=["Objects"])


@router.get("", response_model=List[schemas.ObjectShow])
async def get_objects(db: Database = Depends(get_mongodb)):
    """
    Get all objects.
    This endpoint retrieves a list of all objects stored in the database.
    """

    objects = []

    for obj in db["objects"].find():
        obj["_id"] = str(obj["_id"])
        objects.append(schemas.ObjectShow(**obj))

    return objects


@router.post("")
async def post_objects(body: schemas.Object, db: Database = Depends(get_mongodb)):
    """
    Get all objects.
    This endpoint retrieves a list of all objects stored in the database.
    """

    data = body.dict()

    print(f"Data antes de inserir: {data}")

    result = db["objects"].insert_one(data)

    print(f"Data depois de inserir: {data}")

    obj = db["objects"].find_one(result.inserted_id)
    obj["_id"] = str(obj["_id"])
    return schemas.ObjectShow(**obj)
