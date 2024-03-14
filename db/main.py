from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb+srv://kimwoojin:dnwls12@kimcluster.vi2fpad.mongodb.net/?retryWrites=true&w=majority")
db = client["eoddb"]
collection = db["users"]

@app.get("/users/")
async def read_users():
    users = []
    for user in collection.find({}, {"_id": 0}):
        users.append(user)
    return users