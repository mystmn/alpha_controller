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
            'list': [],
        }

    def start(self):
        list_log = []

        print(config.cl_setup['ProjectName'])
        print(config.cl_setup['ProjectPurpose'])
        print(config.cl_setup['Model'])

        #  Only passes if completed.
        number, command, message = Display().welcome()

        list_log.append("{}, {}".format(number, command))

        NS = NetworkScanner()

        list_log.append("{}".format(NS.process()))

        #  self.log saves entry to our file
        #  @ return [func, list]
        self.log['list'] = list_log
        logs.info(self.log)

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP


        #  Data Harvesting
        #  -> Sites