# Import the necessary modules
from typing import Optional
# Import the User and Task models from the models module
from app.models import User, Task
# Import the UserCreate, UserUpdate, TaskCreate, and TaskUpdate schemas from the schemas module
from app.schemas import UserCreate, UserUpdate, TaskCreate, TaskUpdate

# Define the get_current_user function
async def get_current_user(token: str = Depends(oauth2_scheme)) -> Optional[User]:
    # Get the user from the token
    user = get_user_from_token(token)
    if not user:
        return None
    # Return the user
    return user

# Define the get_user_from_token function
def get_user_from_token(token: str) -> Optional[User]:
    # Split the token into its parts
    token_parts = token.split(".")
    if len(token_parts) != 3:
        return None
    # Decode the token payload
    payload = jwt.decode(token_parts[1], SECRET_KEY, algorithms=[ALGORITHM])
    # Get the user from the payload
    user = get_user(db, payload["sub"])
    if not user:
        return None
    # Return the user
    return user

# Define the get_db function
def get_db() -> Session:
    # Get the database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define the get_user_or_404 function
def get_user_or_404(db: Session, user_id: int) -> User:

    # Get the user from the database session
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the user
    return user

# Define the get_task_or_404 function
def get_task_or_404(db: Session, task_id: int) -> Task:
    # Get the task from the database session
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Return the task
    return task