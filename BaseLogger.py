import inspect
import logging

class BaseLogger():

    def test_logs(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('newlogs.log')
        logFormatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)

        return logger
