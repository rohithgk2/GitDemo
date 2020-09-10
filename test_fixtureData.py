import pytest
from SELENIUM_PRACTICE.Pytest.BaseLogger import BaseLogger

@pytest.mark.usefixtures("importData")
class TestFixturedata(BaseLogger):

    def test_function(self,importData):
        log = self.test_logs()
        log.info(importData[1])
        # print(importData[0])
        log.info(importData[0])