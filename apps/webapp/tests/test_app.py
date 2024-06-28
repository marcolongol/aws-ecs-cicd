from flask.testing import FlaskClient


def test_home_page(client: FlaskClient) -> None:
    """Test that the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data
