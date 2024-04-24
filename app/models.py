# Import the necessary modules
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# Import the Base class from the database module
from app.database import Base

# Define the User model
class User(Base):
    
    # Set the table name
    __tablename__ = "users"

    # Define the columns
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    # Define the relationship with the Task model
    tasks = relationship("Task", back_populates="owner")

# Define the Task model
class Task(Base):
    # Set the table name
    __tablename__ = "tasks"
    # Define the columns
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())

    # Define the relationship with the User model
    owner = relationship("User", back_populates="tasks")
    # Define the string representation of the object
    def __str__(self):
        return f'Task {self.title} by {self.owner.username}'