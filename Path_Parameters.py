from fastapi import FastAPI
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
def read():
    return BOOKS


@app.get("/books/special")
def get_special_book():  # This function contradict with the function present below,It must be defined above as it is
    return BOOKS[0]  # specific otherwise /books/special will call the /book/book_title


@app.get("/books/{book_title}")
def get_specific_book(book_title: str):
    new_books = []
    for book in BOOKS:
        if book["title"].__contains__(book_title):
            new_books.append(book)
    return new_books


@app.post("/{book_title}/{book_author}/{book_month}/{book_year}")
def add_book(book_title: str, book_author: str, book_month: Months, book_year: int):
    new_book = {"title": book_title, "author": book_author, "month": book_month, "year": book_year}
    BOOKS.append(new_book)
    return BOOKS


@app.get("/books/by_month/{book_month}")
def get_book_by_month(book_month: Months):
    selected_month = ""
    match book_month:
        case book_month.dec:  # or you can do match book_month.value  case "January"
            selected_month = book_month
            return f"Wao You Selected my Favorite Month {selected_month}"
        case _:
            selected_month = book_month
            return f"You didn't select my favorite.You choose {selected_month}"


@app.post("/filepath/{file_path:path}")
def send_path_as_path_parameter(file_path:str):    # cant be optional
    return {"Path": file_path}
