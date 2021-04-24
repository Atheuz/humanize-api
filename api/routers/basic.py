"""Basic router."""
from fastapi import APIRouter, status
from starlette.requests import Request
from starlette.responses import JSONResponse

from api.models import basic_models

router = APIRouter()


@router.get("/basic/ping", tags=["basic"], status_code=status.HTTP_200_OK, response_model=basic_models.PingOut)
def ping(request: Request):
    """Ping endpoint."""
    request.app.logger.info("basic-ping")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "pong"})
