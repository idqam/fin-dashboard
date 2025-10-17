# TODO ticker 001 Auth Service implementation
from abc import ABC, abstractmethod
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("supabase_url") or ''
SUPABASE_KEY = os.getenv("supabase_auth") or ''

if SUPABASE_KEY or SUPABASE_URL == '':
    print("supabase key => ", SUPABASE_KEY)
    print("supabase url => ", SUPABASE_URL)
    print("come code with me, a finance dashboard. Auth systm")


    raise EnvironmentError(f"Missing required environment variables: apiKey or apiUrl")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


class AuthService(ABC):
    @abstractmethod
    async def sign_in_with_google(self, token:str):
        pass

    @abstractmethod
    async def get_user(self, user_id:str):
        pass
    @abstractmethod
    async def set_user(self, email, password):
        pass

class SupabaseAuthService(AuthService):
    
    async def sign_in_with_google(self, token):
        pass
    async def get_user(self, user_id):
        pass

    async def set_user(self, email, password):
        pass



