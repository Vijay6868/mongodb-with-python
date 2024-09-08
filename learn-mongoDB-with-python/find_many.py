import os
from dotenv import load_dotenv
from pymongo import MongoClient

import pprint

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

db = client.linkedin_profiles

profiles_collection = db.profiles

dcouments_to_found = {'name.first':'John'}

cursor = profiles_collection.find(dcouments_to_found)

num_docs = 0

for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# documents found" + str(num_docs))

client.close()