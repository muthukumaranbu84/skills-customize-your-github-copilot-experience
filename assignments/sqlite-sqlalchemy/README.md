# 📘 Assignment: Persistent CRUD with SQLite & SQLAlchemy

## 🎯 Objective

Introduce persistent data storage by modeling and performing CRUD operations using SQLite and the SQLAlchemy ORM in Python.

## 📝 Tasks

### 🛠️ Build a small notes manager using SQLAlchemy

#### Description
Create a Python module and CLI that uses SQLAlchemy to store `Note` records in a local SQLite database. Students will define a Pydantic-style model using SQLAlchemy's declarative base, create a database engine and session, and implement functions to create, read, update, and delete notes.

#### Requirements
Completed project should:

- Define a `Note` model with fields `id: int` (primary key), `title: str`, `content: str`, and `created_at: datetime`.
- Create or connect to a local SQLite database file (e.g., `notes.db`).
- Implement and expose functions or CLI commands to:
  - Create a note
  - List all notes (ordered by `created_at`)
  - Retrieve a note by `id`
  - Update a note's title/content
  - Delete a note
- Use SQLAlchemy sessions safely (commit/rollback) and close sessions when done.
- Provide a `starter-code.py` in this folder with a `main()` entry point demonstrating the operations.
- Include a `requirements.txt` listing required packages.

#### Example usage
```
# Create a note
python starter-code.py create --title "Groceries" --content "Buy milk and eggs"

# List notes
python starter-code.py list

# Update a note
python starter-code.py update --id 1 --title "Groceries (updated)"

# Delete a note
python starter-code.py delete --id 1
```

#### How to run

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the starter CLI:

```bash
python starter-code.py --help
```
