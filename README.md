# Library Management API

A FastAPI-based CRUD API for managing books in a PostgreSQL database. The project demonstrates core backend development concepts such as RESTful routing, database integration with SQLAlchemy, data validation with Pydantic, and environment-based configuration.

## Fundamentals Covered

This project covers the following fundamentals:

- REST API development with FastAPI
- CRUD operations for resources
- PostgreSQL database integration using SQLAlchemy
- Request/response validation with Pydantic
- Dependency injection for database sessions
- Environment variable configuration with Python dotenv

## Setup Instructions

### 1. Clone the project

```bash
git clone <your-repository-url>
cd Library_Management
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic python-dotenv
```

### 4. Set up PostgreSQL

Create a PostgreSQL database and update your connection string accordingly.

Example:

- Database name: `books_db`
- Username: `your_db_username`
- Password: `your_db_password`
- Host: `localhost`
- Port: `5432`

### 5. Create a `.env` file

Create a file named `.env` in the project root with your database credentials:

```env
DATABASE_URL=postgresql://your_db_username:your_db_password@localhost:5432/books_db
```

> Replace the values with your own PostgreSQL credentials if needed.

## How to Run

Start the FastAPI application with:

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Retrieve all books or filter by title search term |
| GET | `/books/{id}` | Retrieve a single book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update an existing book |
| DELETE | `/books/{id}` | Delete a book by ID |
| GET | `/health` | Health check endpoint (not currently implemented in the codebase) |

## API Documentation (Swagger UI)

Once the server is running, open the Swagger UI at:

http://127.0.0.1:8000/docs

![Swagger UI](swagger_screenshot.png)
