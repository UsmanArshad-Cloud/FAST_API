from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# Coming back to the previous code example, FastAPI will:
#
# Validate that there is an item_id in the path for GET and PUT requests.
# Validate that the item_id is of type int for GET and PUT requests.
# If it is not, the client will see a useful, clear error.
# Check if there is an optional query parameter named q (as in http://127.0.0.1:8000/items/foo?q=somequery)
# As the q parameter is declared with = None, it is optional.
# Without the None it would be required (as is the body in the case with PUT).
# For PUT requests to /items/{item_id}, Read the body as JSON:
# Check that it has a required attribute name that should be a str.
# Check that it has a required attribute price that has to be a float.
# Check that it has an optional attribute is_offer, that should be a bool, if present.
# All this would also work for deeply nested JSON objects.
# Convert from and to JSON automatically.
# Document everything with OpenAPI, that can be used by:
# Interactive documentation systems.
# Automatic client code generation systems, for many languages.