import httpx

JSON_placeholder = "https://jsonplaceholder.typicode.com"
        
async def get_user_id(id: int):
    """
    Obtiene la información de un usuario por su ID desde JSON_placeholder.

    Args:
        id (int): ID del usuario a obtener.

    Returns:
        dict: Datos del usuario en formato JSON.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JSON_placeholder}/users/{id}")
        response.raise_for_status()
        return response.json()  