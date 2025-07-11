from pydantic import BaseModel, EmailStr

class person(BaseModel):
    id:int
    name: str
    email : EmailStr
    phone_number : int