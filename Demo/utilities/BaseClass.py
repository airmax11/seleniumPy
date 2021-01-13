import logging
import inspect
import pytest

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
