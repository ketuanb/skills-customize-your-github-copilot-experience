# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build fast, modern REST APIs using FastAPI. You'll create a web service with multiple endpoints, implement request validation, and handle different HTTP methods to build a fully functional API.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI Server with Endpoints

#### Description
Set up a FastAPI application with multiple GET and POST endpoints. You'll build the foundation of a simple API that handles different routes and HTTP methods.

#### Requirements
Completed program should:

- Have a root endpoint (`/`) that returns a welcome message
- Have a GET endpoint (`/items/{item_id}`) that returns item data based on the ID
- Have a GET endpoint (`/users`) that returns a list of all users
- Have a POST endpoint (`/users`) that accepts new user data and returns the created user
- Use appropriate HTTP status codes (200 for success, 201 for created)

#### Example Input/Output
```python
# GET /
# Response: {"message": "Welcome to the API"}

# GET /items/42
# Response: {"item_id": 42, "name": "Item 42", "description": "Sample item"}

# POST /users
# Request: {"name": "John Doe", "email": "john@example.com"}
# Response: {"id": 1, "name": "John Doe", "email": "john@example.com"}
```

### 🛠️ Task 2: Implement Request and Response Models with Validation

#### Description
Add Pydantic models to validate incoming requests and structure responses. This ensures your API only accepts valid data and provides consistent responses to clients.

#### Requirements
Completed program should:

- Create Pydantic models for User and Item data
- Validate that required fields are present and have correct types
- Use model validation in POST/PUT endpoints
- Return properly typed responses using the models
- Include field descriptions and examples in model definitions

#### Example
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float

# POST /items with validation
# Request: {"name": "Widget", "price": 9.99}
# Response includes validated model data
```

### 🛠️ Task 3: Add CRUD Operations with Data Persistence

#### Description
Build out full CRUD (Create, Read, Update, Delete) operations for managing data. Store data in memory and implement endpoints for retrieving, updating, and deleting resources.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve a single resource by ID
- Implement POST endpoint to create new resources
- Implement PUT endpoint to update existing resources
- Implement DELETE endpoint to remove resources
- Handle cases where resources don't exist (404 status code)
- Maintain data in memory using a dictionary or list
- Return appropriate HTTP status codes (200, 201, 204, 404)

#### Example
```python
# GET /items/1
# Response: {"id": 1, "name": "Widget", "price": 9.99}

# PUT /items/1
# Request: {"name": "Updated Widget", "price": 12.99}
# Response: {"id": 1, "name": "Updated Widget", "price": 12.99}

# DELETE /items/1
# Response: 204 No Content

# GET /items/1
# Response: 404 Not Found
```
