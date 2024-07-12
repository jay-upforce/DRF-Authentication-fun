import pytest

@pytest.fixture()
def setup():
    print("Fixture Execute..")
    yield
    print("Fixture End...")