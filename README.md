# Secure To-Do Application (Mini CI/CD Project)

This project is a simple secure To-Do web application developed using Python and Flask.
It allows users to add, view, and delete tasks, with data stored persistently using SQLite.
The project demonstrates basic web development, security practices, Docker containerization,
and Continuous Integration using GitHub Actions.

---

## Features
- Add new tasks
- View all tasks
- Delete tasks
- Persistent storage using SQLite
- Input validation and SQL injection prevention
- Dark-themed user interface

---

## Technologies Used
- Operating System: Ubuntu 22.04
- Programming Language: Python 3.12
- Web Framework: Flask
- Database: SQLite
- Containerization: Docker
- CI/CD: GitHub Actions
- Version Control: Git & GitHub

---

## How to Run Locally (Without Docker)

```bash
# Activate virtual environment
source venv/bin/activate

# Run the application
python3 app.py
