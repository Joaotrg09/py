import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
MONGO_URL = os.environ.get("MONGO_URL")
