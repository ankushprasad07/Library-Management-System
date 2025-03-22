Library Management System
Overview
This is a Django Rest Framework (DRF) application designed to manage a library system. The system includes features to manage books, authors, and borrowing processes. Users can borrow and return books, while administrators can manage the library catalog.

Features
1. User Management
User registration with email and password confirmation.
JWT-based authentication for secure access.
Separate permissions for admin users and normal users:
Admins can create, update, and delete books and authors.
Users can borrow and return books.
2. Library Management
CRUD operations for:
Authors.
Books.
Search and filter functionality for books by:
Title (search).
Author (filter).

Clone the repository

Create Virtual environment: py -m venv lib_venv

Activate venv: lib_venv\scripts\activate

Start Project: django-admin startproject library_management

cd library-management

Install dependencies:
pip install -r requirements.txt

Run database migrations:
py manage.py makemigrations
py manage.py migrate

Create a superuser (for admin access): python manage.py createsuperuser

Start the development server: python manage.py runserver

Access the admin panel: http://127.0.0.1:8000/admin/
