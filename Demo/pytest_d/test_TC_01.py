import pytest

@pytest.mark.sanity
@pytest.mark.skip
def test_new_01():
    print("Hello Pytest")

def test_new_02_sanity():
    print("Hello Pytest")

@pytest.mark.sanity
def test_new_03_sanity():
    print("Hello Pytest")