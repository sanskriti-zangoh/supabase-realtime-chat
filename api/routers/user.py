from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from core import load_settings, supabase_client
from api.schemas import User
import bcrypt
from uuid import uuid4
from datetime import datetime, timezone
from api.routers.depends import user_exists

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/signup")
async def signup(user: User):
    """
    Create new user.

    Args:
        user (User): User object.

    Returns:
        dict: User object.
    """
    try:
        user_email = user.email.lower()
        user_hashed_password = bcrypt.hashpw(user.hashed_password, bcrypt.gensalt())

        if user_exists(user_email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists",
            )

        user = supabase_client.from_("users").insert({
            "name": user.name,
            "email": user_email,
            "hashed_password": user_hashed_password,
        })

        if user:
            return {"message": "User created successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user",
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
    
