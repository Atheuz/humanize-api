"""Test the Humanize routes."""


def test_convert(client):
    """Test POST /versus/entity and good GET /versus/entity/<entity_id>."""
    resp = client.get("/api/v1/humanize/integer", params=dict(value=10_000_000, conversion="intword"))
    assert resp.status_code == 200
    assert resp.json() == {"value": 10_000_000, "conversion": "intword", "humanized_value": "10.0 million"}
    assert True
