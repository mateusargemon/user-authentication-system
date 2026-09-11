# User Registration and Login System

A simple user registration and authentication system developed in Python.

## Features

* User registration
* Password confirmation
* Password hashing with SHA-256
* User login
* Password recovery
* Recovery code generation
* User information display
* Input validation

## Requirements

* Python 3.x

## How to Run

```bash
python login.py
```

## How It Works

The program provides a menu with the following options:

1. Register a new user
2. Log in
3. Reset a password using a recovery code
4. View registered user information
5. Exit

During registration, the user's password is hashed before being stored in memory. A six-character recovery code is also generated for password recovery.

## Technologies

* Python
* hashlib
* secrets
* string
