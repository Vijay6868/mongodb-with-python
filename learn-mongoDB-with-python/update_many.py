import os
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.linkedin_profile

profile_collection = db.profile

