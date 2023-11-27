from pydantic import BaseModel, EmailStr
# pip install pydantic[email]
from datetime import datetime, date

class UserBase(BaseModel):
    username: str
    password: str
    email: EmailStr

    # class Config:
    #     json_schema_extra = {
    #         "examples": [
    #             {
    #                 "username": "user01",
    #                 "password": "user01_password",
    #                 "email": "user01@example.com"
    #             }
    #         ]
    #     }

# class PostBase(BaseModel):
#     title: str
#     content: str
#     user_id: int