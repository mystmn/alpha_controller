import logging  ## https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/


class Scribe(object):
    def __init__(self, sys_code="", message=""):
        self.vault(sys_code, message)

    def vault(self, sys_code="", message=""):
        code = {
            100: 'critical',
            200: 'info',
            300: 'debug',
        }

        if isinstance(message, dict):
            for k, v in message.items():
                self.vault(k, v)

        elif isinstance(message, list):
            if [sys_code is k for k, v in code.items()]:
                list(map(getattr(Scribe, code[sys_code]), message))

        else:
            exit("Error {} :: No default.code found".format(__file__))

    @staticmethod
    def info(_list=[]):
        _code = 200
        _file = "info_dump.log"

        # create the logging file handler
        file_handler = logging.FileHandler(_file)

        formatter = logging.Formatter('%(asctime)s,  %(levelname)s,  %(message)s')
        file_handler.setFormatter(formatter)

        logger = logging.getLogger("INFO")
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)

        if isinstance(_list, list):
            [logger.info("{} :: {}".format(str(_code), str(x))) for x in _list]
        elif isinstance(_list, str):
            logger.info("{} :: {}".format(str(_code), str(_list)))
        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))

    def debug(_list=[]):
        _code = 300
        _file = "debug_dump.log"

        # create the logging file handler
        file_handler = logging.FileHandler(_file)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(class_func)s')
        file_handler.setFormatter(formatter)
        logger = logging.getLogger("DEBUG")

        # Setting the record to be written
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        if isinstance(_list, list):
            [logger.debug("{} :: {}".format(str(_code), str(x))) for x in _list]
        elif isinstance(_list, str):
            logger.debug("{} :: {}".format(str(_code), str(_list)))

        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))

    def critical(_list=[]):
        _code = 100
        _file = "critical_dump.log"
        file_handler = logging.FileHandler(_file)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger = logging.getLogger("CRITICAL")
        logger.setLevel(logging.CRITICAL)
        logger.addHandler(file_handler)

        if isinstance(_list, list):
            [logger.critical("{} :: {}".format(str(_code), str(x))) for x in _list]
        elif isinstance(_list, str):
            logger.critical("{} :: {}".format(str(_code), str(_list)))
        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))
