from .progress import progress
from AnkiVector import MONGO_DB_URI
from .tools import human_to_bytes, humanbytes, md5, time_formatter
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient



# MongoDB client
print("[INFO]: INITIALIZING DATABASE")
mongo_client = MongoClient(MONGO_DB_URI)
db = mongo_client.AnkiVector
