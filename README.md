# Python MySQL CRUD Desktop Application

Desktop application for performing CRUD operations (Create, Read, Update, Delete) using Python, Tkinter, and MySQL.

---

## Project Overview

This project is a desktop-based CRUD management system developed in Python, designed to interact with a MySQL relational database through a graphical user interface (GUI).

The application allows users to manage records efficiently by performing the four essential database operations:

- Create new records
- Read and display stored data
- Update existing entries
- Delete records from the database

The graphical interface is built using Tkinter, Python’s standard GUI library, while MySQL serves as the persistent storage layer.

This project demonstrates practical implementation of database-driven desktop applications and core software engineering concepts such as database connectivity, event-driven programming, and user interface design.

---

## Project Objective

The main goal of this application is to provide a functional desktop solution for database record management, integrating Python programming with relational database operations.

This project was created to strengthen practical skills in:

- Python application development
- MySQL database integration
- GUI design
- CRUD logic implementation

---

## Main Features

### Record Management

The system supports complete CRUD operations:

- Add new records into the database
- Display stored information in tabular form
- Edit selected records
- Remove records from the database

### User Interface

The application includes:

- Graphical form inputs
- Interactive table visualization
- Buttons for CRUD actions
- User-friendly workflow
- Input validation

### Database Connectivity

The system connects directly to MySQL and executes SQL queries for:

- INSERT
- SELECT
- UPDATE
- DELETE

---

## Technology Stack

This project is built with:

- Python 3
- Tkinter
- MySQL
- mysql-connector-python
- SQL
- Event-driven programming

---

## Project Architecture

The application follows a simple modular architecture that separates:

---

## Project Structure

```bash
crud_python_mysql/
│
├── main.py              # Application entry point
├── window.py            # Graphical interface logic
├── connectDB.py         # Database connection management
├── DatabaseMySQL/       # SQL scripts / database resources
├── images/              # Interface assets
└── README.md            # Project documentation
```

---

## Functional Description

The application provides a desktop form where users can input information and execute database operations directly.

Typical workflow:

1. User opens the application
2. GUI loads form fields
3. Connection to MySQL database is established
4. Records are displayed
5. User can perform CRUD actions
6. Interface refreshes automatically

---

## Prerequisites

Before running the project, ensure you have installed:

### Required Software

| Requirements |
| ----------- |
| Python 3.10+ |
| MySQL Server |
| MySQL Workbench (optional) |
| Git |

### Required Python Libraries

Install dependencies:

```bash
pip install mysql-connector-python
```

Tkinter is included by default in most Python installations.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/esancanr/crud_python_mysql.git
cd crud_python_mysql
```

---

## Database Setup

Create the database in MySQL:

```sql
CREATE DATABASE crud_python;
```

Create the required table using your SQL script from the repository.

You may import the SQL schema located in:

```bash
DatabaseMySQL/
```

---

## Configuration

Update database credentials in:

```python
connectDB.py
```

Example:

```python
host = "localhost"
user = "root"
password = "your_password"
database = "crud_python"
```

---

## Running the Application

Execute:

```bash
python main.py
```

The graphical interface will launch and allow interaction with the database.

---

## CRUD Operations

### Create

Insert a new record through the form.

### Read

Retrieve and display all records in the table.

### Update

Select a record and update its fields.

### Delete

Select a record and remove it permanently.

---

## Technical Concepts Demonstrated

This project showcases implementation of:

- GUI programming
- Database integration
- Relational data management
- SQL operations
- Modular code organization

---

## Practical Skills Demonstrated

This repository highlights experience in:

- Python programming
- Tkinter GUI development
- MySQL integration
- CRUD application design
- Backend fundamentals
- Data persistence
- User interface handling
- Software modularization

---

## Real-World Applications

This type of project can be adapted for:

- Student management systems
- Inventory systems
- Employee management
- Customer records
- Administrative desktop tools
- Internal business software

---

### Suggested Files

```bash
requirements.txt
.gitignore
.env.example
```

---

## Author

Developed by Edison Sancan

Information Technology Engineer  
Python | MySQL | Desktop Applications | Backend | DevOps
