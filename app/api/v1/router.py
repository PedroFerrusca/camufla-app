# app/api/v1/router.py

from fastapi import APIRouter

from app.api.v1.endpoints import router as healthcheck_router

router = APIRouter()

# later
router.include_router(healthcheck_router)
# router.include_router(games.router)
