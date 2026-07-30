# Student Management System

## Overview

Student Management System is an intermediate-level Python project designed to manage student records efficiently.

This project is developed using Python, Object-Oriented Programming (OOP) concepts, modular package structure, and SQLite Database for permanent data storage.

The system allows users to add, view, search, update, and delete student records.

## Features

- Add Student Records
- View All Student Details
- Search Student by Roll Number
- Update Student Information
- Delete Student Records
- Store Data Permanently using SQLite Database
- Modular Python Package Structure
- Object-Oriented Programming Implementation

## Technologies Used

- Python 3
- SQLite Database
- Object-Oriented Programming (OOP)
- Python Modules and Packages

## Project Structure

Student-Management-System
│
├── main.py
│
└── student_management_system
    │
    ├── __init__.py
    ├── student.py
    ├── database.py
    └── operation.py


## File Description

### main.py
- Provides menu-driven user interface
- Controls the complete application flow

### student.py
- Contains Student class
- Implements Object-Oriented Programming concepts

### database.py
- Handles SQLite database connection
- Creates student table
- Performs database operations

### operation.py
- Contains business logic
- Handles add, view, search, update, and delete operations

## Functionalities

### 1. Add Student

- Add new student details into the database
- Stores student information permanently

### 2. View Students

- Displays all student records stored in the database

### 3. Search Student

- Search student details using student ID or roll number

### 4. Update Student

- Modify existing student information

### 5. Delete Student

- Remove student records from the database

## Database

SQLite database is used for storing student information permanently.

### Student Table

| Column | Description |
|---|---|
| ID | Unique student identifier |
| Name | Student name |
| Age | Student age |
| Course | Student course |

## How to Run

### Clone Repository git clone github-link(https://github.com/chanthuru258/Student-Management-System-Python.git)

1. Download or clone this repository.

2. Open the project in VS Code or any Python IDE.

3. Open the terminal in the project folder.

4. Run the following command:

```bash
python main.py
```


## Future Enhancements

- User Login Authentication
- GUI Application using Tkinter
- Web Application using Flask/Django
- Export Student Data to Excel/PDF

## Author

Chanthuru S
    

## Project Structure
