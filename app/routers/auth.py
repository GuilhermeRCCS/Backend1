# Import required modules

from fastapi import APIRouter, Depends, HTTPException

from typing import Optional


# Import custom modules

from app.models import User

from app.schemas import UserCreate, UserDB

from app.utils import hash_password, get_user_by_email

from app.config import SECRET_KEY, ALGORITHM


# Initialize the router

router = APIRouter()


# Define the route for creating a new user

@router.post("/register", response_model=UserDB)

async def register(user: UserCreate):

    # Check if the user already exists

    existing_user = await get_user_by_email(user.email)

    if existing_user:

        raise HTTPException(status_code=400, detail="Email already registered")


    # Hash the password

    user.password = hash_password(user.password)


    # Create a new user

    new_user = User(**user.dict())

    await new_user.save()


    # Generate a JWT token

    access_token = create_access_token(data={"sub": new_user.id}, secret_key=SECRET_KEY, algorithm=ALGORITHM)


    # Return the user and token

    return {"user": new_user, "access_token": access_token}


# Define the route for logging in a user

@router.post("/login", response_model=UserDB)

async def login(user: UserCreate):

    # Get the user from the database

    db_user = await get_user_by_email(user.email)

    if not db_user:

        raise HTTPException(status_code=400, detail="Invalid email or password")


    # Check if the password is correct

    if not hash_password(user.password) == db_user.password:

        raise HTTPException(status_code=400, detail="Invalid email or password")


    # Generate a JWT token

    access_token = create_access_token(data={"sub": db_user.id}, secret_key=SECRET_KEY, algorithm=ALGORITHM)


    # Return the user and token

    return {"user": db_user, "access_token": access_token}


# Define the route for getting the current user

@router.get("/me", response_model=UserDB)

async def me(current_user: User = Depends(get_current_active_user)):

    return current_user


# Define the route for updating the current user

@router.put("/me", response_model=UserDB)

async def update_me(user_update: UserUpdate, current_user: User = Depends(get_current_active_user)):

    # Update the user

    current_user.update_from_dict(user_update.dict())

    await current_user.save()


    return current_user


# Define the route for deleting the current user

@router.delete("/me")

async def delete_me(current_user: User = Depends(get_current_active_user)):
    pass