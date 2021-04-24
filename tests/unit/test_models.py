"""Unit testing models."""
import pytest
from pydantic import ValidationError

from api.models import basic_models, humanize_models


def test_basic_models_good_inputs():
    """Test creating a PingOut with good inputs."""
    assert basic_models.PingOut(detail="pong").dict() == {"detail": "pong"}


def test_basic_models_bad_inputs():
    """Test creating a PingOut with bad inputs."""
    with pytest.raises(ValidationError):
        basic_models.PingOut().dict()


@pytest.mark.parametrize(
    "case,expected",
    [
        ({"value": 10_000_000, "conversion": "intword"}, "10.0 million"),
        ({"value": 10_000_000, "conversion": "intcomma"}, "10,000,000"),
        ({"value": 10_000_000, "conversion": "apnumber"}, "10000000"),
        ({"value": 10_000_000, "conversion": "ordinal"}, "10000000th"),
        ({"value": 10_000_000, "conversion": "scientific"}, "1.00 x 10⁷"),
    ],
)
def test_humanize_models_good_inputs(case, expected):
    """Test creating an IntegerOut with good inputs."""
    assert humanize_models.IntegerOut(**case).humanized_value == expected


@pytest.mark.parametrize(
    "case, error_msg",
    [
        ({"value": 10_000_000, "conversion": "invalid"}, "unexpected value"),  # invalid conversion field value
        ({"value": 10_000_000}, "field required"),  # missing conversion field
        ({"value": "abc", "conversion": "intword"}, "value is not a valid integer"),  # invalid value field value
        ({"valuea": 10_000_000}, "field required"),  # missing all fields
        ({"conversion": "intword"}, "field required"),  # missing value field
    ],
)
def test_humanize_models_bad_inputs(case, error_msg):
    """Test creating an IntegerOut with bad inputs."""
    with pytest.raises(ValidationError) as exc:
        humanize_models.IntegerOut(**case)
    assert error_msg in exc.value.json()
