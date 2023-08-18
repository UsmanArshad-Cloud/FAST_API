from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from typing import Optional, Dict, Any

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(title="Description of the Book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(lt=101, gt=-1)


BOOKS = [
    Book(
        id="2e10da95-9af7-4a48-9caa-56a4926204be",
        title="Book Title 1",
        author="Author 1",
        description="Description of Book 1",
        rating=80
    ),
    Book(
        id="67d7a048-a072-462b-8804-4efdd7f0279e",
        title="Book Title 2",
        author="Author 2",
        description="Description of Book 2",
        rating=95
    ),
    Book(
        id="b56fb91e-e08a-4529-adf2-748a0f01a5de",
        title="Book Title 3",
        author="Author 3",
        description="Description of Book 3",
        rating=95
    ),
]


@app.get("/")
def read_book():
    return BOOKS


@app.get("/get_int/{int_input}")
def get_int(int_input) -> int:
    return int_input


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user

# OR

#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(BaseUser):
#     password: str
#
#
# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user