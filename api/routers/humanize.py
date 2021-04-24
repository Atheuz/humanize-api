"""Humanize endpoints."""
from fastapi import APIRouter, Query, status
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing_extensions import Literal

from api.models import humanize_models

router = APIRouter()


@router.get(
    "/humanize/integer",
    tags=["humanize"],
    response_model=humanize_models.IntegerOut,
    status_code=status.HTTP_200_OK,
)
def convert_integer(
    request: Request,
    value: int = Query(..., description="The integer to convert"),  # noqa: B008
    conversion: Literal["intcomma", "intword", "apnumber", "ordinal", "scientific"] = Query("intword"),  # noqa: B008
):
    """Create a new Integer conversion."""
    out = jsonable_encoder(humanize_models.IntegerOut(value=value, conversion=conversion))
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=out,
    )
