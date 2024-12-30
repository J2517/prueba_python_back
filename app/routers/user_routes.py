from fastapi import APIRouter
from typing import Dict, Any
from app.Services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/users/{user_id}", response_model=Dict[str, Any])
async def get_user(user_id: int):
    return await user_service.get_user(user_id)

@router.get("/posts", response_model=Dict[str, Any])
async def get_posts():
    return await user_service.get_posts()
