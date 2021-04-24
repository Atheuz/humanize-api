"""Define humanize models."""
from typing import Optional

import humanize
from pydantic import BaseModel, Field, validator
from typing_extensions import Literal


class Integer(BaseModel):
    """Match model."""

    value: int = Field(..., description="Integer value", example=10000000000000000000)
    conversion: Literal["intcomma", "intword", "apnumber", "ordinal", "scientific"] = Field(
        ..., description="Conversion type", example="intword"
    )


class IntegerOut(Integer):
    """Integer Out model."""

    humanized_value: Optional[str] = Field(
        None,
        description="The humanized value.",
        example="10.0 quintillion",
    )

    @validator("humanized_value", pre=False, always=True)
    def validate_humanized_value(cls, v, values, **kwargs):
        """Validate humanized_value."""
        if "conversion" not in values:
            return None
        if "value" not in values:
            return None
        fn = getattr(humanize, values["conversion"])
        return fn(values["value"])
