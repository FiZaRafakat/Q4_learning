from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None 

user_data = {"id": 526123, "name": "Fiza", "email": "fiza@example.com", "age": 20}
user = User(**user_data)
print(user) 
print(user.model_dump())  

try:
    invalid_user = User(id="not_an_int", name="Maheen", email="maheen@example.com")
except ValidationError as e:
    print(e)
    
