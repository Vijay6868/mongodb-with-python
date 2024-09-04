
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint
import os

from bson.objectid import ObjectId

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)

db = client.linkedin_profiles

profiles_collection = db.profiles

document_to_find = {"_id": ObjectId("66d77eda905e1a3ba148768d")}

result = profiles_collection.find_one(document_to_find)

pprint.pprint(result)

client.close()