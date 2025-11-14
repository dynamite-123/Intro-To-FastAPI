# Intro to FastAPI

A simple FastAPI application demonstrating basic CRUD operations for a book management system.

## Features

- Create, read, update, and delete books
- Search for borrowed books
- Pydantic models for request/response validation
- Automatic API documentation with Swagger UI

## Prerequisites

- Python 3.7 or higher
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dynamite-123/Intro-To-FastAPI.git
cd Intro-To-FastAPI
```

### 2. Create and Activate Virtual Environment

#### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### macOS

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install "fastapi[all]"
```

### 4. Run the Application(outside app dir)

```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API Documentation**: http://localhost:8000/docs

## API Endpoints

### Books

- `GET /` - Welcome message
- `GET /books` - Get all books
- `GET /books/{book_id}` - Get a specific book by ID
- `POST /books/create` - Create a new book
- `PUT /books/update/{book_id}` - Update an existing book
- `DELETE /books/delete/{book_id}` - Delete a book
- `GET /borrowed` - Get all borrowed books

## Project Structure

```
.
├── main.py          # FastAPI application and routes
├── schemas.py       # Pydantic models
└── README.md        # Project documentation
```

## Data Models

### Book (Input)
- `title`: string
- `author`: string  
- `is_borrowed`: boolean (default: false)

### BookOut (Response)
- `id`: integer
- `title`: string
- `author`: string
- `is_borrowed`: boolean

## Development

To deactivate the virtual environment when done:

```bash
deactivate
```

## Additional Notes

- The application uses an in-memory list to store books, so data will be lost when the server restarts
- Book IDs are automatically generated when creating new books
- All endpoints include proper response models for API documentation and validation
