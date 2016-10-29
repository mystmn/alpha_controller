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

        self.settler['elogger']

        LogCaller().write_file(__name__, "Go bucks!")

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP

        #  Data Harvesting
        #  -> Sites