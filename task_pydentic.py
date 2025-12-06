from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date


class Address(BaseModel):
    street: str
    city: str
    pincode: int  
    
class User(BaseModel):
    first_name: str  
    last_name: str
    full_name: str = Field(..., alias="fullName") 
    email: str
    phone: Optional[str] = None
    age: int
    registered_at: date
    skills: List[str]
    address: Address

    @field_validator("age")
    def age_must_be_18_or_above(cls, v):
        if v < 18:
            raise ValueError("User must be at least 18 years old")
        return v

    @field_validator("skills")
    def skills_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("At least one skill must be provided")
        return v

raw_json = {
    "first_name": "Sachin",
    "last_name": "Kharat",
    "fullName": "Sachin Kharat",
    "email": "sachin@example.com",
    "age": "22",
    "phone": None,
    "registered_at": "2024-12-01",
    "skills": ["python", "selenium", "fastapi"],
    "address": {
        "street": "Palm Avenue",
        "city": "Mumbai",
        "pincode": "400001"
    }
}

user = User.model_validate(raw_json)
print(user.model_dump(by_alias=True))

