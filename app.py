from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: User):

    logging.info(f"Creating user: {user.email}")

    if "@" not in user.email:
        raise HTTPException(
            status_code=400,
            detail="Invalid email"
        )

    return {
        "message": "User created",
        "user": user
    }

# ADD THIS BELOW
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "User found"
    }