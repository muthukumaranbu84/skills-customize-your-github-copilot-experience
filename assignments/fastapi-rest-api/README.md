# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple REST API using the FastAPI framework, Pydantic models, and basic HTTP methods (GET, POST, PUT, DELETE).

## 📝 Tasks

### 🛠️ Implement a REST API for a simple resource (Notes)

#### Description
Create a FastAPI application that exposes CRUD endpoints for a `Note` resource. Use Pydantic models for request/response validation and an in-memory store (e.g., a list or dict) for persistence while the app is running.

#### Requirements
Completed project should:

- Include a `Note` Pydantic model with at least `id: int`, `title: str`, and `content: str` fields.
- Implement endpoints:
  - `GET /notes` — return a list of all notes
  - `GET /notes/{id}` — return a single note or 404
  - `POST /notes` — create a new note (return 201)
  - `PUT /notes/{id}` — update an existing note or 404
  - `DELETE /notes/{id}` — delete a note or 404
- Validate request bodies using Pydantic models and return appropriate HTTP status codes.
- Use simple in-memory storage (no external database required).
- Provide a `starter-code.py` with a `main()` entry point to run the app.
- Include a `requirements.txt` listing needed packages.

#### Example requests and responses
```
POST /notes
Body: {"title":"Shopping","content":"Buy milk"}
Response: 201 Created

GET /notes
Response: [{"id":1,"title":"Shopping","content":"Buy milk"}]

GET /notes/1
Response: {"id":1,"title":"Shopping","content":"Buy milk"}
```

#### How to run

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app:

```bash
python starter-code.py
# or: uvicorn starter-code:app --reload
```
