from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for creating new tasks
class TaskCreate(BaseModel):
    # The title of the task
    title: str
    # The description of the task (optional)
    description: Optional[str] = None
    # Whether the task is completed (optional)
    completed: Optional[bool] = False

# Define a Pydantic model for updating existing tasks
class TaskUpdate(BaseModel):
    # The new title of the task (optional)
    title: Optional[str] = None
    # The new description of the task (optional)
    description: Optional[str] = None
    # Whether the task is completed (optional)
    completed: Optional[bool] = None

# Define a Pydantic model for returning tasks to the user
class Task(BaseModel):
    # The ID of the task
    id: int
    # The title of the task
    title: str
    # The description of the task (optional)
    description: Optional[str] = None
    # Whether the task is completed
    completed: bool
    # The ID of the user who owns the task
    owner_id: int

    # Configure the model to use ORM mode
    class Config:
        orm_mode = True