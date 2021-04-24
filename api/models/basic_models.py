"""Define basic models."""
from pydantic import BaseModel, Field


class PingOut(BaseModel):
    """Ping definition."""

    detail: str = Field(..., example="pong")
