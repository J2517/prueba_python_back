from fastapi import APIRouter, HTTPException
import httpx
from app.Services.user_service import get_user_id
from app.Services.user_service import get_posts_user
from datetime import datetime
import logging

router = APIRouter()

logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
   filename='app.log',
    filemode='a'
)

logger = logging.getLogger(__name__)


@router.get("/users/{id}")
async def get_user(id: int):
    try:
        logger.info(f"Iniciando solicutud para usuario ID: {id}")
        user = await get_user_id(id)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Usuario ID {id} encontrado exitosamente")
        response = {
            "user": user,
            "date": date
            }
        return response
    except httpx.HTTPError as e:
        logger.error(f"Error al obtener usuario {id}: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Error al obtener usuario: {str(e)}")
    except Exception as e:
        logger.error(f"Error interno: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    