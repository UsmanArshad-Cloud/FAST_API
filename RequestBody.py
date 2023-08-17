from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

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
def get(skip: int = 0, limit: int = 2):
    new_books = []
    for i in range(skip + limit):
        if skip <= i <= limit and skip + limit <= len(BOOKS):
            new_books.append(BOOKS[i])
    return new_books


@app.post("/")
def create_book(book: Book):
    BOOKS.append(book)


@app.put("/")
def update_book(id: UUID, updated_book: Book):
    index = 0
    for book in BOOKS:
        if book.id == id:
            BOOKS[index] = updated_book
        index += 1
    return BOOKS

