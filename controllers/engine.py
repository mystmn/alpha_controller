import config.main as config
from helpers.logs import LogCaller
from helpers.menu import MainMenu as MM


class Main(object):
    def __init__(self):
        self.settler = {
            'elogger': [],
        }

    def start(self):
        print(config.cl_setup['ProjectName'])
        print(config.cl_setup['ProjectPurpose'])
        print(config.cl_setup['Model'])

        number, command, message = MM().display()

        print("{} | {} | {}".format(number, command, message))

        x = LogCaller
        x.informative('INFO', "Testing of the log")
        #  Commands to send out among the network to gather
        #  -> Models, Names, IP

        #  Data Harvesting
        #  -> Sites
