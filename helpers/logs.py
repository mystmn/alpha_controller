import logging  ## https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/


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


def info(cl_func='NULL'):
    """ insert[debug, critical, info], save classer and message to file """

    # create the logging file handler
    file_handler = logging.FileHandler("dump.log")

    formatter = logging.Formatter('%(asctime)s,  %(levelname)s,  %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger("INFO")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    if isinstance(cl_func['list'], list):

        # message, func, list
        for each_message in cl_func['list']:
            logger.info("cf({}), list({})".format(str(cl_func['func']), str(each_message)))

    elif isinstance(cl_func['list'], dict):

        for k, v in cl_func['list'].items():
            logger.info("cf({}), dict({}: {})".format(str(cl_func['func']), str(k), str(v)))

    else:
        logger.info("cf({}), str({})".format(str(cl_func['func']), str(cl_func['list'])))
