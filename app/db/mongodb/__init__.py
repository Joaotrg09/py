from pymongo import MongoClient

from app.config import MONGO_URL


def get_mongodb():
    client = MongoClient(MONGO_URL)
    db = client["capivara"]

    return db
