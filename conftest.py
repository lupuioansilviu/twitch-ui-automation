import pytest
from src.core.driver_factory import create_driver


@pytest.fixture(scope="function")
def driver():
    d = create_driver()
    yield d
    d.quit()