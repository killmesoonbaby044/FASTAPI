from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    email: EmailStr
    created_at: datetime
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
# dir=1 add vote dir=0 delete vote


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # id: str | None = None
    id: Optional[str] = None
