
from pydantic_settings import BaseSettings


class Settings(BaseSettings): 
    PROJECT_NAME: str = "Finance Dashboard Backend"
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",  
    ]

    SUPABASE_URL: str
    SUPABASE_KEY: str 

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings() # type: ignore
