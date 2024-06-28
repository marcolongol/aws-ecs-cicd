from typing import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from webapp import create_app


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = create_app()
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
