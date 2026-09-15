# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, a modern Python web framework for creating fast and scalable APIs. In this assignment, you will create endpoints that accept input, return JSON responses, and follow common API patterns.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a minimal FastAPI app and create a route that returns a JSON response for a simple health check or list of items.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define at least one GET endpoint
- Return JSON data in a readable structure
- Run the app with a local development server

### 🛠️ Add CRUD API Endpoints

#### Description
Build routes for creating, reading, updating, and deleting items in a small in-memory collection.

#### Requirements
Completed program should:

- Define routes for listing and creating items
- Allow fetching a single item by ID
- Support updating an existing item
- Support deleting an item
- Return responses with JSON payloads and appropriate status codes

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API by validating incoming data and handling invalid requests gracefully.

#### Requirements
Completed program should:

- Use Pydantic models to define request data
- Validate required fields before processing requests
- Return a 404 response when an item is not found
- Return helpful error messages for invalid input
- Keep the API easy to test with browser or client requests
