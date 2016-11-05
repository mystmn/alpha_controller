import logging ## https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/


def debug(x='NULL'):
    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(class_func)s')
    file_handler.setFormatter(formatter)
    logger = logging.getLogger("DEBUG")

    # Setting the record to be written
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    if isinstance(x, dict):
        length_message = "{} - {}".format(x['log'], x['message'])
    else:
        length_message = "{} - {}".format(bool(False), bool(False))

    logger.debug(length_message)


def critical(message='NA'):
    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("CRITICAL")
    logger.setLevel(logging.CRITICAL)
    logger.addHandler(file_handler)
    logger.critical(message)


def info(class_function='NULL'):
    """ insert[debug, critical, info], save classer and message to file """

    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s,  %(levelname)s,  %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("INFO")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    if isinstance(class_function, dict):
        if not class_function.get('message'):
            length_message = "cf({}), e('Message': \"Not Set\")".format(str(class_function['func']))
        else:
            length_message = "cf({}), m({})".format(str(class_function['func']), str(class_function['message']))
    else:
        length_message = "cf({}), e({})".format(str(class_function['func']), bool(False))

    logger.info(length_message)
