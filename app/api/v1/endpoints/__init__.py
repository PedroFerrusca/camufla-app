# app/api/v1/endpoints/__init__.py
from datetime import datetime
from typing import Any

from fastapi import APIRouter

from app import __version__

router = APIRouter()


@router.get("/healthcheck", status_code=200, description="Healthcheck")
def healthcheck() -> dict[str, Any]:
    return {"status": "ok", "app_name": "camufla", "version": __version__, "time": datetime.now()}
