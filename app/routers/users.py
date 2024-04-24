from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas import UserCreate, UserOut, Token
from app.models import User
from app.utils import get_db, hash_password, verify_password
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.dependencies import get_current_active_user, get_current_active_superuser

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """

    Create a new user.

    """

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create a new user with the hashed password
    db_user = User(email=user.email, password=hashed_password, is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    """

    Authenticate a user and return an access token.

    """

    # Get the user from the database
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verify the password
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create an access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_active_user)):

    """

    Get the current active user.

    """

    return current_user

@router.get("/users/me/items/", response_model=list[Item])
def read_own_items(current_user: User = Depends(get_current_active_user)):

    """

    Get items that belong to the current active user.

    """

    return [item for item in items if item.owner_id == current_user.id]

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, current_user: User = Depends(get_current_active_superuser)):

    """

    Get a user by ID.

    """

    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user