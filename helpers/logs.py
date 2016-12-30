import logging  # https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/
import random
# We need to create multiple sessions..
# .. https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook


class Scribe(object):
    def __init__(self, sys_code="", message=""):
        self.past = None
        self.vault(sys_code, message)

    def vault(self, sys, message=""):
        code = {
            100: 'critical',
            200: 'info',
            300: 'debug',
        }

        if isinstance(message, dict):
            for k, v in message.items():
                self.vault(k, v)

        elif isinstance(message, list):
            if [sys is k for k, v in code.items()]:
                list(map(getattr(Scribe, code[sys]), message))

        elif isinstance(message, str):
            _function = getattr(Scribe, code[sys])
            _function(message)

        else:
            exit("Error {} :: No default.code found".format(__file__))

        self.past = True

    @staticmethod
    def info(x=""):
        _code = 200
        _file = "info_dump.log"

        #  Random is needed to create a new logger session, if not it'll create duplicates
        logger = logging.getLogger("INFO.{}".format(random.random()))


        file_handler = logging.FileHandler(_file)

        formatter = logging.Formatter('%(asctime)s,  %(levelname)s,  %(message)s')
        file_handler.setFormatter(formatter)

        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)

        if isinstance(x, str):
            logger.info("{} :: {}".format(str(_code), str(x)))
        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))

    @staticmethod
    def debug(x=[]):
        _code = 300
        _file = "debug_dump.log"

        #  Random is needed to create a new logger session, if not it'll create duplicates
        logger = logging.getLogger("DEBUG".format(random.random()))

        file_handler = logging.FileHandler(_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(class_func)s')
        file_handler.setFormatter(formatter)

        # Setting the record to be written
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        if isinstance(x, str):
            logger.critical("{} :: {}".format(str(_code), str(x)))
        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))

    @staticmethod
    def critical(x=[]):
        _code = 100
        _file = "critical_dump.log"
        #  Random is needed to create a new logger session, if not it'll create duplicates
        logger = logging.getLogger("CRITICAL.{}".format(random.random()))

        file_handler = logging.FileHandler(_file)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.setLevel(logging.CRITICAL)
        logger.addHandler(file_handler)

        if isinstance(x, str):
            logger.critical("{} :: {}".format(str(_code), str(x)))
        else:
            exit("Error {} - {} :: Wrapping code in a list".format(_code, __file__))
