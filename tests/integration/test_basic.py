"""Test the Basic routes."""


def test_ping(client):
    """Test GET /basic/ping."""
    resp = client.get("/api/v1/basic/ping")

    assert resp.status_code == 200
    assert resp.json() == {"detail": "pong"}


def test_ping_bad(client):
    """Test POST /basic/ping."""
    resp = client.post("/api/v1/basic/ping")

    assert resp.status_code == 405
    assert resp.json() == {"detail": "Method Not Allowed"}
