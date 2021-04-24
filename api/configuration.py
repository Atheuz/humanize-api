"""Configuration."""
import os

import dotenv
from pydantic import BaseModel

dotenv.load_dotenv()  # Only loads if there is a .env file present.


class BaseConfig(BaseModel):
    """Base configuration."""

    # Meta config
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    VERSION: str = open(os.path.join(BASE_DIR, "VERSION")).read().strip()
    ENVIRONMENT: str = "production"

    # API config
    API_NAME: str = "humanize"
    API_PREFIX: str = "/api/v1"
    OPENAPI_URL: str = "openapi.json"
    DOCS_URL: str = "docs"
    REDOC_URL: str = "redocs"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    ENVIRONMENT: str = "development"


class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENVIRONMENT: str = "testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENVIRONMENT: str = "production"


def from_envvar():
    """Get configuration class from ENVIRONMENT env variable."""
    options = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }
    choice = os.environ.get("ENVIRONMENT", "testing")
    if choice not in options:
        raise ValueError(f"ENV={choice} is not valid, must be one of {options}")
    loaded_config = options[choice](**os.environ)
    return dict(loaded_config)
