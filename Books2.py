from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = Field(title="Description of the Book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(lt=101, gt=-1)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "5deb2d42-6ecf-4c48-9504-9eab928c914d",
                "title": "Book Title",
                "author": "A very good author",
                "description": "A very nice description of Book",
                "rating": 0
            }
        }


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
]


@app.get("/")
async def read_all_books(books_to_read: Optional[int] = None):
    if books_to_read and 0 <= books_to_read <= len(BOOKS):
        new_books = []
        for i in range(books_to_read):
            new_books.append(BOOKS[i])
            i += 1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return None


@app.post("/")
async def createBook(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    counter = 0
    for book in BOOKS:
        if book.id == book_id:
            BOOKS[counter] = book
            return BOOKS[counter]
        counter += 1


@app.delete("/{book_id}")
async def delete_book(book_id: UUID):
    counter = 0
    for book in BOOKS:
        if book.id == book_id:
            del BOOKS[counter]
        counter += 1
