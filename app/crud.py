# Import the necessary modules
from sqlalchemy.orm import Session
# Import the User and Task models from the models module
from app.models import User, Task
# Import the UserCreate, UserUpdate, TaskCreate, and TaskUpdate schemas from the schemas module
from app.schemas import UserCreate, UserUpdate, TaskCreate, TaskUpdate

# Define the get_user function
def get_user(db: Session, user_id: int):
    # Return the user with the given ID from the database session
    return db.query(User).filter(User.id == user_id).first()

# Define the get_users function
def get_users(db: Session):
    # Return all users from the database session
    return db.query(User).all()

# Define the create_user function
def create_user(db: Session, user: UserCreate):
    # Create a new user with the given data and add it to the database session
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Define the update_user function
def update_user(db: Session, user_id: int, user: UserUpdate):
    # Get the user with the given ID from the database session
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    # Update the user's data with the given data
    db_user.username = user.username
    db_user.password = user.password
    # Commit the changes to the database session
    db.commit()
    return db_user

# Define the delete_user function
def delete_user(db: Session, user_id: int):

    # Get the user with the given ID from the database session
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    # Remove the user from the database session
    db.delete(db_user)
    db.commit()
    return db_user

# Define the get_task function
def get_task(db: Session, task_id: int):

    # Return the task with the given ID from the database session
    return db.query(Task).filter(Task.id == task_id).first()

# Define the get_tasks function
def get_tasks(db: Session):

    # Return all tasks from the database session
    return db.query(Task).all()

# Define the create_task function
def create_task(db: Session, task: TaskCreate):
    
    # Create a new task with the given data and add it to the database session
    db_task = Task(title=task.title, description=task.description, owner_id=task.owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Define the update_task function
def update_task(db: Session, task_id: int, task: TaskUpdate):
    
    # Get the task with the given ID from the database session
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    # Update the task's data with the given data
    db_task.title = task.title
    db_task.description = task.description

    # Commit the changes to the database session
    db.commit()
    return db_task

# Define the delete_task function
def delete_task(db: Session, task_id: int):
    # Get the task with the given ID from the database session
    db_task = get(db_task)