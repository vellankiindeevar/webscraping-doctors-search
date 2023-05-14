import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]
collection = db["mycollection"]

with open('doctors.json', 'r') as f:
    data = json.load(f)

collection.insert_many(data)
