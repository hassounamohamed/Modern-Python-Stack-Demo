# FastAPI Tutorial

from fastapi import FastAPI, Query, HTTPException
from typing import List
from pydantic import BaseModel

# Create an app
app = FastAPI()

# Define a path for HTTP GET method
@app.get("/")
def root():
    return {"Hello": "World"}

# GET and POST Routes
items = []

@app.post("/items")  # Fixed: added missing leading slash
def create_item(item: str):
    items.append(item)
    return item

@app.get("/items/{item_id}")  # Fixed: added missing leading slash
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item

# Handling HTTP Errors
@app.get("/items/error/{item_id}")  # Changed path to avoid route conflict
def get_item_with_error(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]  # Fixed: removed "="
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# JSON Request and Path Parameters
@app.get("/items/")
def list_items(limit: int = 10):
    return items[0:limit]

# Pydantic models
class Item(BaseModel):
    text: str = None
    is_done: bool = False

# Response Models
@app.get("/items_list", response_model=List[Item])  # Changed path to avoid duplicate
def list_item(limit: int = 10):
    return items[0:limit]  # Added missing return statement

@app.get("/items_model/{item_id}", response_model=Item)  # Changed path to avoid conflict
def get_item_model(item_id: int) -> Item:
    return items[item_id]  # This assumes `items` is a list of Item objects
