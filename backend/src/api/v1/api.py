from fastapi import APIRouter
from . import auth, todos

# Main API router that includes all version 1 endpoints
router = APIRouter()

# Include the auth and todos routers
router.include_router(auth.router, prefix="", tags=["auth"])
router.include_router(todos.router, prefix="", tags=["todos"])