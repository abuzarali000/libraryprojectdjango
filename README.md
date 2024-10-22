# Library Project Django

## Overview

This is a Django-based library management system designed to manage a collection of books. The project provides a RESTful API for interacting with the book collection, allowing users to perform operations such as adding, retrieving, updating, and deleting books. 

## Features

- Add, update, delete, and retrieve books.
- Filter books by author and language.
- Pagination for book listings.
- User-friendly API endpoints.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abuzarali000/libraryprojectdjango.git
   
2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Configure the database:

Create a new MySQL database (e.g., library_db).
Update the database settings in settings.py with your MySQL configuration.

4. Run migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver


6. Access the APIs:

The API will be available at http://127.0.0.1:8000/api/books/.

API Endpoints
GET /api/books/: List all books with optional filtering.
POST /api/books/: Add a new book to the collection.
GET /api/books/<id>/: Retrieve details of a specific book.
PUT /api/books/<id>/: Update an existing book.
DELETE /api/books/<id>/: Remove a book from the collection.
