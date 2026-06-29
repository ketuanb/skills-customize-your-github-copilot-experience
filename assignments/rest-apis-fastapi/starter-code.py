"""
FastAPI Starter Code - Building REST APIs with FastAPI

This is your starting point for building a REST API with FastAPI.
Complete the tasks by implementing the required endpoints and functionality.

To run this application:
1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://localhost:8000/docs to see the interactive API documentation
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(
    title="REST API with FastAPI",
    description="A learning project for building REST APIs",
    version="1.0.0"
)

# TODO: Task 2 - Create Pydantic models for request/response validation
# Uncomment and implement the User and Item models below:
"""
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
"""

# TODO: Task 3 - Create in-memory storage for data
# Uncomment and initialize data structures:
"""
# Store users and items in memory
users_db: List[dict] = []
items_db: List[dict] = []
next_user_id: int = 1
next_item_id: int = 1
"""

# Task 1: Basic Endpoints

@app.get("/", tags=["root"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    # TODO: Return a welcome message as a dictionary
    pass


@app.get("/items/{item_id}", tags=["items"])
def get_item(item_id: int):
    """
    Get an item by its ID.
    """
    # TODO: Return item data for the given ID
    pass


@app.get("/users", tags=["users"])
def list_users():
    """
    Get a list of all users.
    """
    # TODO: Return list of all users
    pass


@app.post("/users", tags=["users"], status_code=status.HTTP_201_CREATED)
def create_user(user_data: dict):
    """
    Create a new user.
    """
    # TODO: Accept user data and return the created user with an ID
    pass


# Task 2 & 3: Add your endpoints here for request/response models and CRUD operations
# TODO: Add more endpoints as needed for complete CRUD functionality


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
