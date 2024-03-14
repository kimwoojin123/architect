from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

db_server_url = "http://127.0.0.1:8001"


@app.get("/")
async def root():
  return { "message" : "hello, World"}

@app.get("/users")
async def read_users():
    try:
        response = requests.get(f"{db_server_url}/users")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))