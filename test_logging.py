import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)  #creating an object for logging class __name__ specifies the testcase name
    fileHandler = logging.FileHandler("logfile.log") #creating object for fileHandler ->specifies the filepath of logreport
    logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(logFormat)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    logger.debug("This is the debug message")
    logger.info("This is the info message")
    logger.warning("This is the warning section")
    logger.error("This is an error message")
    logger.critical("This is a critical error")
