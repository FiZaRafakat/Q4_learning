from pydantic import BaseModel, EmailStr, validator, ValidationError

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: list[Address]

    @validator("name")
    def name_must_be_at_least_four_chars(cls, v):
        if len(v) < 4:
            raise ValueError("Name must be at least 4 characters long")
        return v

try:
    invalid_user = UserWithAddress(
        id=73846,
        name="F", 
        email="fiza@example.com",
        addresses=[{"street": "789 Pine Rd", "city": "Chicago", "zip_code": "60601"}],
    )
except ValidationError as e:
    print(e)