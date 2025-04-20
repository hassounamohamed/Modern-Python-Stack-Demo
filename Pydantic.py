from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

user = User(
    name = "Salah",
    email = "salah@gmail.com",
    account_id = 12345
)

print(user.name)
print(user.email)
print(user.account_id)

#Validating Data with Pydantic
from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr     # pip install pydantic[email]
    account_id: int


user = User(name = 'Ali', email = 'ali', account_id = 1234)
print(user)

#Custom Field Validation
@field_validator("account_id")
def validate_account_id(cls, value):
    if value <= 0:
        raise ValueError(f"account_id must be positive: {value}")
    return value
user = User(name = 'Ali', email = 'ali@gmail.com', account_id = 12)
print(user)

#JSON Serialization
user_json_str = user.model_dump_json()
print(user_json_str)

#Pydantic vs Dataclasses
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int
user = User(name = 'Ali', email = 'ali@gmailcom', account_id = 'hello')
print(user)