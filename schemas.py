from pydantic import BaseModel
from pydantic import BaseModel, EmailStr

class BookCreate(BaseModel):
    title: str
    author: str
    is_published: bool = True

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"