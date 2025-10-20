# TODO ticker 001 Auth Service implementation
import os
import logging
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from supabase import AsyncClient, acreate_client
from supabase_auth import AuthResponse, User
from app.core.config import settings

from app.core.config import Settings

logger = logging.getLogger(__name__)

load_dotenv()



async def init_supabase_client() -> AsyncClient:
    """Initialize and return the Supabase async client."""
    client = await acreate_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_KEY
    )
    return client


class AuthService(ABC):
    """Abstract authentication interface."""

    @abstractmethod
    async def sign_in_with_google(self, token: str) -> AuthResponse:
        pass

    @abstractmethod
    async def get_user(self, user_id: str) -> User:
        pass

    @abstractmethod
    async def set_user(self, email: str, password: str) -> AuthResponse: 
        pass


class SupabaseAuthService(AuthService):
    """Supabase-backed implementation of AuthService."""

    def __init__(self, client: AsyncClient):
        self.client = client

    async def sign_in_with_google(self, token: str):
        response = await self.client.auth.sign_in_with_id_token(
            {"provider": "google", "token": token}
        )
        if response.user is None:
            logger.warning("Google sign-in failed.")
        return response

    async def get_user(self, user_id: str) -> User:
        response = await self.client.auth.admin.get_user_by_id(user_id)
        return response.user

    async def set_user(self, email: str, password: str) -> AuthResponse:
        response = await self.client.auth.sign_up(
            {"email": email, "password": password}
        )
        if response.user is None:
            logger.warning(f"User creation failed for {email}")
        return response
