
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)

db = client.linkedin_profiles

profiles_collection = db.profiles

new_profile = {
    "name": {
    "first": "John",
    "last": "Wick"
  },
  "contact_info": {
    "email": "john.doe@example.com",
    "linkedin_url": "https://www.linkedin.com/in/johndoe"
  },
  "experience": [
    {
      "title": "Senior Software Engineer",
      "company": "XYZ Company",
      "location": "San Francisco, CA",
      "start_date": "2020-05-01",
      "end_date": "Present",
      "description": "Lead the development of new features for the XYZ platform..."
    },
    {
      "title": "Software Engineer",
      "company": "ABC Inc.",
      "location": "New York, NY",
      "start_date": "2017-06-01",
      "end_date": "2020-04-30",
      "description": "Developed and maintained web applications using React and Node.js..."
    }
  ],
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "institution": "University of California, Berkeley",
      "start_date": "2013-08-01",
      "end_date": "2017-05-01",
      "location": "Berkeley, CA"
    }
  ]

}

result = profiles_collection.insert_one(new_profile)

document_id = result.inserted_id

print(f"_id for inserted document: {document_id}")

client.close()