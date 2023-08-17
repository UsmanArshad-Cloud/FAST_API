from fastapi import FastAPI, Query
from typing import Optional, Annotated
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
async def get(skip: Annotated[int, Query(le=len(BOOKS), ge=0)] = 0,
              limit: Annotated[int, Query(le=len(BOOKS), ge=0)] = len(BOOKS)):
    index = 0
    new_books = []
    for book in BOOKS:
        if skip <= index <= limit:
            new_books.append(book)
        index += 1
    return new_books
