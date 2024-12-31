import pytest
from unittest.mock import Mock, patch
from fastapi import HTTPException
import httpx
from app.Services.user_service import UserService
from app.Services.user_state import UserState


@pytest.fixture
def user_service():
    """Fixture crea una instancia de UserService"""
    return UserService()

# Tests for UserState
def test_singleton_pattern():
    """Test comprobar que ambas referencias apuntan al mismo objeto"""
    instance1 = UserState()
    instance2 = UserState()
    assert instance1 is instance2


@pytest.mark.asyncio
async def test_get_user_http_error(user_service):
    """Test manejo de errores para el usuario"""
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.get.side_effect = \
            httpx.HTTPError("HTTP Error")
        
        with pytest.raises(HTTPException) as exc_info:
            await user_service.get_user(1)
        
        assert exc_info.value.status_code == 500
        assert "Error al obtener datos del usuario" in str(exc_info.value.detail)

@pytest.mark.asyncio
async def test_get_posts_without_user(user_service):
    """Test obtener posts sin consultar usuario"""
    with pytest.raises(HTTPException) as exc_info:
        await user_service.get_posts()
    
    assert exc_info.value.status_code == 400
    assert "Debe consultar primero un usuario" in str(exc_info.value.detail)

@pytest.mark.asyncio
async def test_get_posts_success(user_service):
    """Testobtener correctamente los posts"""
    test_user = {"id": 1, "name": "Test User"}
    test_posts = [
        {"userId": 1, "id": 1, "title": "Post 1"},
        {"userId": 1, "id": 2, "title": "Post 2"}
    ]
    
    user_service.user_state.set_last_user(1, test_user)
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_response = Mock()
        mock_response.json.return_value = test_posts
        mock_response.raise_for_status = Mock()
        
        mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
        
        result = await user_service.get_posts()
        
        assert "Date" in result
        assert result["user_info"] == test_user
        assert result["posts"] == test_posts
        assert result["post_count"] == 2

@pytest.mark.asyncio
async def test_get_posts_http_error(user_service):
    """Test posts retrieval with HTTP error"""
    test_user = {"id": 1, "name": "Test User"}
    user_service.user_state.set_last_user(1, test_user)
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.get.side_effect = \
            httpx.HTTPError("HTTP Error")
        
        with pytest.raises(HTTPException) as exc_info:
            await user_service.get_posts()
        
        assert exc_info.value.status_code == 500
        assert "Error al obtener las publicaciones" in str(exc_info.value.detail)