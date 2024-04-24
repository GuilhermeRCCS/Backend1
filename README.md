Purpose of the Application:

The FastAPI Task Management System is a web-based application that allows users to manage tasks, including creating, updating, and deleting tasks, as well as assigning tasks to users and tracking their progress. The application is designed to be easy to use and highly scalable, making it ideal for managing tasks in a variety of settings.

-------------------------------------------------------------------------------------------------------------------------------

Technical Justification for the Choice of Frameworks:

The application is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is designed to be highly productive, allowing developers to build APIs quickly and easily, while also being highly performant, making it ideal for building scalable applications.

In addition to FastAPI, the application uses Django for authentication and Click for command-line interface. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design, while Click is a Python package for creating beautiful command line interfaces.

-------------------------------------------------------------------------------------------------------------------------------

Installation Process

  Clone the repository: git clone https://github.com/GuilhermeRCCS/Backend1.git
  Navigate to the project directory: cd fastapi-task-management
  Create a virtual environment: python -m venv venv
  Activate the virtual environment: source venv/bin/activate (on Linux/macOS) or venv\Scripts\activate (on Windows)
  Install the dependencies: pip install -r requirements.txt
  Create a .env file with the following variables:

DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

  Run the database migrations: alembic upgrade head
  Start the application: uvicorn app.main:app --reload

-------------------------------------------------------------------------------------------------------------------------------

How to Use the Application

To use the FastAPI Task Management System, follow these steps:

    Open a web browser and navigate to http://localhost:8000
    Log in using the credentials provided in the .env file
    Create a new task by clicking the "Create Task" button
    Update an existing task by clicking the "Edit" button next to the task
    Delete a task by clicking the "Delete" button next to the task
    Assign a task to a user by selecting the user from the "Assigned To" dropdown
    Track the progress of a task by updating the "Progress" field