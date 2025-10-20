from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def signup(request: Request, body: dict):
    """Create a new user using Supabase Auth."""
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return JSONResponse(
            status_code=400, content={"error": "Email and password are required."}
        )

    auth_service = request.app.state.auth_service
    response = await auth_service.set_user(email, password)

    if not response.user:
        return JSONResponse(status_code=400, content={"error": "Signup failed."})

    return {"message": "Signup successful", "user": response.user.email}
