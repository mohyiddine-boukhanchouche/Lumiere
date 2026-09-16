from pydantic import BaseModel, Field
from typing import Annotated
from datetime import date


class UserCreate(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=50)]
    password: Annotated[str, Field(min_length=6)]
    birthday: Annotated[date, Field(description=("Date of birth, format YYYY-MM-DD"))]


class Userlogin(BaseModel):
    username: Annotated[str, Field(min_length=1, max_length=200)]
    password: Annotated[str, Field(min_length=3)]


class userresponse(BaseModel):
    id: int
    name: str


class Cchat(BaseModel):
    Question: str


class error_life(BaseModel):
    detail: str
