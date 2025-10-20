from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.auth_api import router
from app.core.middleware import setup_middleware
from app.services.auth_service import SupabaseAuthService, init_supabase_client



@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase_client = await init_supabase_client()
    app.state.auth_service = SupabaseAuthService(app.state.supabase_client)
    print("✅ Supabase client initialized.")

    yield

    print(" Application shutdown complete (no persistent connections).")

app = FastAPI(lifespan=lifespan)
setup_middleware(app)
app.include_router(router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
