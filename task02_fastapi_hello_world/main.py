from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World" : "From Fiza"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}! Welcome to FastAPI!"}