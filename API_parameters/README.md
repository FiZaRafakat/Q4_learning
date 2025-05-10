# 📚 FastAPI API Parameters - Beginner Guide

Welcome! 🚀  
Here’s a quick and clear way to understand **how APIs receive information** using FastAPI, with real examples.

---

## 📌 1. Path Parameters

Use when a part of the URL should change (like selecting an item).

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```
🔗 Visit `/items/5` → Returns item with ID 5.

## 📌 2. Query Parameters

Use for optional filters or settings, added after ? in the URL.
```
@app.get("/items/")
async def list_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```
🔗 Visit `/items?skip=5&limit=10`.

## 📌 3. Request Body 

Send structured data (usually JSON), like forms or login info.
```
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(user: User):
    return {"message": f"Welcome {user.username}!"}
```
📦 Send JSON in the body.

## 📌 4. Headers

Send extra hidden data like device info or tokens.
```
from fastapi import Header

@app.get("/get-header/")
async def get_header(user_agent: str = Header(default=None)):
    return {"Your-User-Agent": user_agent}
```
🛡️ Reads data from HTTP headers.

## 📌 5. Cookies

Store small data like user sessions between visits.
```
from fastapi import Cookie, Response

@app.get("/set-cookie/")
async def set_cookie(response: Response):
    response.set_cookie(key="mycookie", value="delicious")
    return {"message": "Cookie has been set"}

@app.get("/get-cookie/")
async def get_cookie(mycookie: str = Cookie(default=None)):
    return {"mycookie": mycookie}
```
🍪 Set and get cookies.

## 📌 6. Form Data

Send classic HTML form fields.
```
from fastapi import Form

@app.post("/submit-form/")
async def submit_form(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}
```
📝 Used for traditional form submissions.

## 📌 7. File Uploads

Send files like images or documents.
```
from fastapi import UploadFile, File

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    return {"filename": file.filename, "content_size": len(content)}
```
📂 Upload and handle files.

# 💬 Bonus Tip:

Just run `http://127.0.0.1:8000/docs` — FastAPI gives you a free UI to test everything easily!
