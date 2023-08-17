from typing import Optional

from fastapi import FastAPI
from enum import Enum

app = FastAPI()
BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author 2'},
    'book_3': {'title': 'Title Three', 'author': 'Author 3'},
    'book_4': {'title': 'Title Four', 'author': 'Author 4'},
    'book_5': {'title': 'Title Five', 'author': 'Author 5'},
}


class DirectionName(Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get("/")
async def main_fun():
    return BOOKS;

@app.get("/books/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS.values():
        print("Required", book_title)
        print("Ours", book["title"])
        if book["title"] == book_title:
            return book


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    elif direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Down"}
    elif direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Left"}
    else:
        return {"Direction": direction_name, "sub": "Right"}


@app.post("/")
async def CreateBook(book_title, book_author):
    curr_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            X = int(book.split('_')[-1])
            if X > curr_book_id:
                curr_book_id = X
    BOOKS[f'book_{curr_book_id + 1}'] = {'title': book_title, 'author': book_author}
    return BOOKS[f'book_{curr_book_id + 1}']


@app.put("/")
async def UpdateBook(book_name: str, book_title: str, book_author: str):
    book_information = {'title': book_title, 'author': book_author}
    BOOKS[book_name] = book_information
    return BOOKS[book_name]


# Using Query Parameter
@app.delete("/")
async def DeleteBook(book_name):
    del BOOKS[book_name]
    return BOOKS


# Using Path Parameter
@app.delete("/{book_name}")
async def DeleteBook(book_name):
    del BOOKS[book_name]
    return BOOKS
