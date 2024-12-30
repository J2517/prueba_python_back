import httpx
from fastapi import HTTPException
from datetime import datetime
from .user_state import UserState

class UserService:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.user_state = UserState()

    async def get_current_datetime(self) -> str:
        """
        Obtiene la fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS"
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    async def get_user(self, user_id: int):
        """
        Obtiene la información de un usuario por su ID desde la API de JSONPlaceholder.
        Args:
            user_id (int): ID del usuario a consultar
            
        Returns:
            dict: Información del usuario  
            
        Raises:
            HTTPException: Error al obtener datos del usuario          
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/users/{user_id}")
                response.raise_for_status()
                user_data = response.json()

            self.user_state.set_last_user(user_id, user_data)

            return {
                "Date": await self.get_current_datetime(),
                "user": user_data
            }

        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener datos del usuario {user_id}: {str(e)}")

    async def get_posts(self):
        """
        Obtiene las publicaciones del último usuario consultado.
        Returns:
            dict: Información de la publicaciones por usuario obtenido
        Raises:
            HTTPException: Error al obtener las publicaciones
        """
        try:
            if not self.user_state.has_user():
                raise HTTPException(
                    status_code=400,
                    detail="Debe consultar primero un usuario usando el endpoint /users/{id}"
                )

            last_user = self.user_state.get_last_user()
            user_id = last_user["id"]

            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.base_url}/posts", params={"userId": user_id})
                response.raise_for_status()
                posts = response.json()

            return {
                "Date": await self.get_current_datetime(),
                "user_info": last_user["data"],
                "posts": posts,
                "post_count": len(posts)
            }

        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener las publicaciones: {str(e)}")
