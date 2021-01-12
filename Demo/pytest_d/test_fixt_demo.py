import pytest
from Demo.imp.BaseClass import Baseclass

@pytest.mark.usefixtures("setup", "dataload")
class TestSuit(Baseclass):
    def test_fixture_tests_01(self, dataload):
        log = self.getlogger()
        log.info(dataload)

        print("This is test fixture sample")

    def test_fixture_tests_02(self, dataload):
        print(dataload)

    def test_fixture_tests_03(self):
        print("This is test fixture sample")