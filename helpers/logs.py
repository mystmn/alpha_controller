import logging
import os.path
import datetime


class LogCaller(object):
    def __init__(self):
        pass

    @staticmethod
    def informative(x={}, message='NA'):
        """
          The main entry point of the application
          """

        if x.upper() == "INFO":
            print(x)

            logger = logging.getLogger("INFO")
            logger.setLevel(logging.INFO)

        elif x.upper() == "CRITICAL":
            logger = logging.getLogger("CRITICAL")
            logger.setLevel(logging.CRITICAL)

        else:
            logger = logging.getLogger("DEBUG")
            logger.setLevel(logging.DEBUG)

        # create the logging file handler
        fh = logging.FileHandler("dump.log")

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)

        if x.upper() == "INFO":
            logger.info("Program started")

        elif x.upper() == "CRITICAL":
            logger.critical("HAHA!")

        else:
            pass

if __name__ == "__main__":
    LogCaller.informative()