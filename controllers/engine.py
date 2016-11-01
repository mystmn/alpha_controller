import config.main as config
from helpers import logs
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

        logs.debug("And blah, blah, blah!")
        logs.info("And blah, blah, blah!")

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP

        #  Data Harvesting
        #  -> Sites
