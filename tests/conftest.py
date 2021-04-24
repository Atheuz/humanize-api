"""Set up testing fixtures."""
import pytest
from starlette.testclient import TestClient

from api import factory


@pytest.fixture(scope="function")
def app():
    """Set up an instance of the api."""
    api = factory.create_api()
    return api


@pytest.fixture(scope="function")
def client(app):
    """Set up a requests test client."""
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="function")
def default_headers():
    """Set up default headers."""
    headers = {"Content-Type": "application/json", "User-Agent": "test-agent"}
    return headers
