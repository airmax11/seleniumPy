import logging


def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler("test_run.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    logger.addHandler(filehandler)
    filehandler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.debug("Debug statement executed")
    logger.info("Information statement")
    logger.warning("Warning info")
    logger.error("Error occurred")
    logger.critical("Critical error occurred")
