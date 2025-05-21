from fastapi import FastAPI, Form, Header, Cookie, UploadFile, File, Response
from pydantic import BaseModel

app = FastAPI()

# Request Body Example
class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(user: User):
    return {"message": f"Welcome {user.username}"}


