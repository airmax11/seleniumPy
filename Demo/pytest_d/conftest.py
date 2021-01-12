import pytest
from requests import request


@pytest.fixture(scope="class")
def setup():
    print("Test Case started")
    yield
    print("Test Case Ended")


@pytest.fixture(scope="class")
def dataload():
    print("Test Case started")
    return "BLABLABLA"


@pytest.fixture(params=[("Chrome", "AirMax"), ("mozilla", "Test"), ("IE", "New")])
def sentparameters(request):
    return request.param
