import logging
import datetime


class LogCaller(object):
    def write_file(self, func='N/A', message=''):
        x = datetime.datetime.now().strftime("%y")
        logging.basicConfig(filename=x + ".log", level=logging.INFO, filemode="w")
        """
        The main entry point of the application
        """
        logger = logging.getLogger(func)
        logger.setLevel(logging.INFO)

        # create the logging file handler
        fh = logging.FileHandler("notification.log")

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object
        logger.addHandler(fh)

        logger.info("Program started")
        logger.info("Done!")


if __name__ == "__main__":
    LogCaller().write_file()


    def cldebug(self, messsage="NA"):
        #  Create a file log
        self.write_file(logging.debug(messsage))


    def information(self, message="NA"):
        logging.info(message)


    def e_log(self, message="NA"):
        logging.error(message)
