# Import the FastAPI library
from fastapi import FastAPI
# Import the CORSMiddleware middleware from FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import the routers for authentication, tasks, and users
from app.routers import auth, tasks, users
# Import the User and Task models
from app.models import User, Task
# Import the get_db function for obtaining a database session
from app.utils import get_db
# Import the Pydantic schemas for UserCreate, UserUpdate, TaskCreate, and TaskUpdate
from app.schemas import UserCreate, UserUpdate, TaskCreate, TaskUpdate
# Import the Session class from sqlalchemy.orm
from sqlalchemy.orm import Session

# Initialize the FastAPI app
app = FastAPI()

# Define the allowed origins for CORS
origins = [

    "http://localhost",

    "http://localhost:3000",

]

# Add CORSMiddleware to the app with the allowed origins, credentials, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a route for creating a new task
@app.post("/db", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Create a new Task object with the provided title and description, and set the owner_id to 1
    db_task = Task(title=task.title, description=task.description, owner_id=1)
    # Add the new Task object to the database session
    db.add(db_task)
    # Commit the changes to the database
    db.commit()
    # Refresh the object to get its database-generated ID
    db.refresh(db_task)
    # Return the new Task object
    return db_task

# Define a route for retrieving the current user's information
@app.get("/users/me", response_model=User)
def read_users_me(db: Session = Depends(get_db)):
    # Return a dummy User object with the username "john_doe"
    return {"username": "john_doe"}

# Define a route for logging in as a user
@app.post("/token", response_model=dict)
def login(user: User, db: Session = Depends(get_db)):
    # Check if the provided username and password are correct
    if user.username != "john_doe" or user.password != "password":
        # If not, raise an HTTPException with a 400 status code and a message
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # Set the access token to expire after a certain number of minutes
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Create an access token with the user's username and the specified expiration time
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    # Return the access token and its type as a dictionary
    return {"access_token": access_token, "token_type": "bearer"}

# Define a route for refreshing an access token
@app.post("/token/refresh", response_model=dict)
def refresh_token(user: User, db: Session = Depends(get_db)):
    # Check if the provided username is correct
    if user.username != "john_doe":
        # If not, raise an HTTPException with a 400 status code and a message
        raise HTTPException(status_code=400, detail="Incorrect username")
    # Set the access token to expire after a certain number of minutes
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Create a new access token with the user's username and the specified expiration time
    access_token = create_access