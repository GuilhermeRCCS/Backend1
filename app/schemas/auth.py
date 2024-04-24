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

# Define a Pydantic model for storing the username of the user associated with a token
class TokenData(BaseModel):
    # The username of the user
    username: str

# Define a Pydantic model for returning the access token and token type to the user
class Token(BaseModel):
    # The access token
    access_token: str
    # The token type
    token_type: str