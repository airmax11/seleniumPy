import pytest


@pytest.mark.usefixtures("setup", "dataload")
class TestSuit:
    def test_fixture_tests_01(self):
        print("This is test fixture sample")

    def test_fixture_tests_02(self, dataload):
        print(dataload)

    def test_fixture_tests_03(self):
        print("This is test fixture sample")