from pydantic import BaseModel , EmailStr 

class Address(BaseModel):
    street : str
    city : str
    zip_code : str
    
    
class UserWithAddress(BaseModel):
    id : int 
    email : EmailStr
    name : str
    addresses : list[Address]
    
    
user_data = {
    "id" : 64342 , 
    'email'  : "fiza@gmail.com",
    'name' : "Fiza", 
    'addresses' : [
        {
            'street' : "123 Main St",
            'city' : "New York",
            'zip_code' : "10001"
        },
        {
            'street' : "456 Elm St",
            'city' : "Los Angeles",
            'zip_code' : "90001"
        }
    ]
}
    
    
user = UserWithAddress.model_validate(user_data)
print(user.model_dump_json(indent= 2))