from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for creating new users
class UserCreate(BaseModel):
    # The username of the user
    username: str
    # The password of the user
    password: str

# Define a Pydantic model for updating existing users
class UserUpdate(BaseModel):
    # The new password of the user (optional)
    password: Optional[str] = None

# Define a Pydantic model for returning users to the user
class User(BaseModel):
    # The ID of the user
    id: int
    # The username of the user
    username: str

    # Configure the model to use ORM mode
    class Config:
        orm_mode = True