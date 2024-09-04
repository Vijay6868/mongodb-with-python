from pymongo import MongoClient
from dotenv import load_dotenv

import os
import pprint

from bson.objectid import ObjectId

load_dotenv

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.linkedin_profiles

profile_collection = db.profiles

new_name = {'$set':{'name.last':'Wick'}}

document_to_update = {"_id":ObjectId("66d62195ef420162eddd7db6")}

result = profile_collection.update_one(document_to_update, new_name)

pprint.pprint(profile_collection.find_one(document_to_update))

client.close()