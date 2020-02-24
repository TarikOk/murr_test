import pytest


@pytest.fixture(scope="function")
def app():
    yield
