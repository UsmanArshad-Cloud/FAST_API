from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

BOOKS = [
    {"title": "Book Title 1", "author": "Author 1", "month": "January", "year": 2020},
    {"title": "Book Title 2", "author": "Author 2", "month": "February", "year": 2015},
    {"title": "Book Title 3", "author": "Author 3", "month": "April", "year": 1998},
    {"title": "Book Title 4", "author": "Author 4", "month": "December", "year": 2005},
    {"title": "Book Title 5", "author": "Author 5", "month": "September", "year": 2019}
]


class Months(str, Enum):
    jan = "January"
    feb = "February"
    mar = "March"
    apr = "April"
    may = "May"
    jun = "June"
    jul = "July"
    aug = "August"
    sep = "September"
    oct = "October"
    nov = "November"
    dec = "December"


@app.get("/")
async def get():
    return BOOKS


@app.put("/")
async def Update_Book(to_update_book_title: str, new_book_title: Optional[str] = None, new_book_author: str = None,
                      new_book_month: Months = None, new_book_year: int = None):
    index = 0
    for book in BOOKS:
        if book["title"] == to_update_book_title:
            new_book = {"title": new_book_title if new_book_title else book["title"],
                        "author": new_book_author if new_book_author else book["author"],
                        "month": new_book_month if new_book_month else book["month"],
                        "year": new_book_year if new_book_year else book["year"]}
            BOOKS[index] = new_book
            return BOOKS[index]
        index += 1


@app.delete("/")
async def DeleteBook(book_title: str):
    index = 0
    for book in BOOKS:
        if book["title"] == book_title:
            del BOOKS[index]
        index += 1
    return BOOKS
