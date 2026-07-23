# Library Management API

A FastAPI-based CRUD API for managing books in a PostgreSQL database, secured with JWT authentication. The project demonstrates core backend development concepts such as RESTful routing, database integration with SQLAlchemy, data validation with Pydantic, password hashing, JWT-based auth, and environment-based configuration.

## Fundamentals Covered

This project covers the following fundamentals:

- REST API development with FastAPI
- CRUD operations for resources
- PostgreSQL database integration using SQLAlchemy
- Request/response validation with Pydantic
- Dependency injection for database sessions
- Environment variable configuration with Python dotenv
- User authentication with JWT (JSON Web Tokens)
- Password hashing with passlib (bcrypt)
- Protected routes using FastAPI dependencies
- Associating resources (books) with the authenticated user

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
pip install -r requirements.txt
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

Create a file named `.env` in the project root with your database credentials and auth settings:

```env
DATABASE_URL=postgresql://your_db_username:your_db_password@localhost:5432/books_db
SECRET_KEY=your_random_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Replace the values with your own PostgreSQL credentials and a securely generated secret key. You can generate one with:
> ```bash
> python -c "import secrets; print(secrets.token_hex(32))"
> ```

## How to Run

Start the FastAPI application with:

```bash
uvicorn main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Authentication

This API uses JWT bearer tokens for authentication.

1. **Sign up** via `POST /signup` with an email and password.
2. **Log in** via `POST /login` with the same credentials to receive an `access_token`.
3. Include the token on protected requests as a header: `Authorization: Bearer <access_token>`.
4. Tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default 30 minutes), after which you'll need to log in again.

In Swagger UI, click the **Authorize** button and paste your token to test protected endpoints directly from the browser.

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|:---:|-------------|
| POST | `/signup` | No | Register a new user |
| POST | `/login` | No | Log in and receive a JWT access token |
| GET | `/books` | No | Retrieve all books or filter by title search term |
| GET | `/books/{id}` | No | Retrieve a single book by ID |
| POST | `/books` | **Yes** | Create a new book, associated with the logged-in user |
| PUT | `/books/{id}` | No | Update an existing book |
| DELETE | `/books/{id}` | No | Delete a book by ID |

## API Documentation (Swagger UI)

Once the server is running, open the Swagger UI at:

http://127.0.0.1:8000/docs

![Swagger UI](swagger_books_ui.jpeg)

## After JWT Auth:

![Swagger UI](swagger_ui_jwt.jpeg)

## Developed By

Abdul Hadi
