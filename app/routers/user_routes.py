from fastapi import APIRouter, HTTPException
import httpx
from app.Services.user_service import get_user_id

router = APIRouter()

@router.get("/users/{id}")
async def get_user(id: int):
    try:
        user = await get_user_id(id)
        return user
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuario: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")