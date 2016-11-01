import logging ## https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/


def debug(message='NA'):
    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger = logging.getLogger("DEBUG")

    # Setting the record to be written
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.debug(message)


def critical(message='NA'):
    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("CRITICAL")
    logger.setLevel(logging.CRITICAL)
    logger.addHandler(file_handler)
    logger.critical(message)


def info(message='NA'):
    """ insert[debug, critical, info], save classer and message to file """

    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("INFO")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.info(message)