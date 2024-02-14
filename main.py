from uuid import UUID
from fastapi import FastAPI, HTTPException

from logger import get_logger
from config import DATA_FILE_PATH
from load_data import get_lookup_data


app = FastAPI()
logger = get_logger("server")
lookup = get_lookup_data(DATA_FILE_PATH)


@app.get("/")
def read_root():
    """
    Check if the server is up and running.
    """
    return {"message": "Server is up and running!"}


@app.get("/items/{item_id}")
def read_item(item_id: UUID):
    """
    if uuid is valid and present in lookup: returns 200 with answer
    if uuid is invalid: returns 422 invalid user data
    if uuid is valid not not in lookup: returns 404 not found
    """
    if item_id in lookup:
        return {item_id: lookup[item_id]}
    raise HTTPException(
        status_code=404,
        detail=f"Item with ID {item_id} not found",
    )
