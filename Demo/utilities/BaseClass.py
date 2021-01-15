import logging
import inspect
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Baseclass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("test_run.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        logger.addHandler(filehandler)
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger

    def wait_for_element_and_click(self, key):
        # wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, key)))
        self.driver.find_element_by_link_text(key).click()
