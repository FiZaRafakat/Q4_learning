from fastapi import FastAPI, Path, Query, Body, HTTPException, Form, Header, Cookie, UploadFile, File, Response
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for item validation
class Item(BaseModel):
    name: str
    description: str | None = None  # Optional field
    price: float

# Path Parameter Example
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,  # Required parameter
        title="The ID of the item",  # Metadata for documentation
        description="A unique identifier for the item",  # Description for docs
        ge=1  # Validation: must be greater than or equal to 1
    )
):
    # Return the item ID as a response
    return {"item_id": item_id}

# Query Parameter Example 
@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,  # Optional query parameter
        title="Query string",  # Metadata for documentation
        description="Query string for searching items",  # Description for docs
        min_length=3,  # Validation: minimum length
        max_length=50  # Validation: maximum length
    ),
    skip: int = Query(0, ge=0),  # Default value 0, must be >= 0
    limit: int = Query(10, le=100)  # Default value 10, must be <= 100
):
    # Return query parameters as a response
    return {"q": q, "skip": skip, "limit": limit}

# Request Body Example
@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),  # Path parameter with validation
    q: str | None = Query(None, min_length=3),  # Optional query parameter with validation
    item: Item | None = Body(None, description="Optional item data (JSON body)")  # Optional request body
):
    result = {"item_id": item_id}  # Initialize response with item_id
    if q:
        result.update({"q": q})  # Add query parameter to response if provided
    if item:
        result.update({"item": item.model_dump()})  # Add item data to response if provided
    return result

# Header Example
@app.get("/get-header/")
async def get_header(user_agent: str = Header(default=None)):  # Extract 'User-Agent' header
    return {"Your-User-Agent": user_agent}  # Return the header value

# Cookie Example
@app.get("/set-cookie/")
async def set_cookie(response: Response):  # Use Response object to set a cookie
    response.set_cookie(key="mycookie", value="delicious")  # Set a cookie
    return {"message": "Cookie has been set"}  # Confirm cookie was set

@app.get("/get-cookie/")
async def get_cookie(mycookie: str = Cookie(default=None)):  # Extract cookie value
    return {"mycookie": mycookie}  # Return the cookie value

# Form Data Example
@app.post("/submit-form/")
async def submit_form(name: str = Form(...), age: int = Form(...)):  # Extract form data
    return {"name": name, "age": age}  # Return form data as a response

# File Upload Example
@app.post("/upload/")
async def upload(file: UploadFile = File(...)):  # Handle file upload
    content = await file.read()  # Read file content
    return {"filename": file.filename, "content_size": len(content)}  # Return file info