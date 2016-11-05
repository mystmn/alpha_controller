import config.main as config
from helpers import logs
from helpers.menu import Display
from helpers.nmap import NetworkScanner


class Main(object):
    def __init__(self):
        #  helpers.logs.[info, debug, critical] RETURN ['func', 'message']
        self.log = {
            'func':
                __name__ + "_start",
            'message': False,
        }

    def start(self):
        print(config.cl_setup['ProjectName'])
        print(config.cl_setup['ProjectPurpose'])
        print(config.cl_setup['Model'])

        #  Only passes if completed.
        number, command, message = Display().welcome()

        self.log['message'] = "User chose {} for command {}".format(number, command)
        logs.info(self.log)
        #  self.log saved logs to file
        #  self.log {'func', 'message'}

        NetworkScanner.process()
        #  Commands to send out among the network to gather
        #  -> Models, Names, IP


        #  Data Harvesting
        #  -> Sites
