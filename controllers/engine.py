import config.main as config
from helpers import logs
from helpers.menu import Display
from helpers.nmap import NetworkScanner
from models import setup_config as SC, project


class Main(object):
    def __init__(self):
        #  helpers.logs.[info, debug, critical] RETURN ['func', 'message']
        self.log = {
            'func':
                __name__ + "_start",
            'list': [],
        }

    def start(self):
        logger = []

        print(config.cl_setup['ProjectName'])
        print(config.cl_setup['ProjectPurpose'])
        print(config.cl_setup['Model'])

        #  Only passes if completed.
        number, command, message = Display().welcome()

        # logger.append("{}, {}".format(number, command))

        # logger.append("{}".format(NetworkScanner().route_gateway()))

        project_schema = project.Engine().db_schema()

        print(project_schema)
        print(project_schema)
        print(project_schema)

        DBC = SC.DbController(config.cl_setup['Model'] + "main.db", project_schema)

        DBC_SELECT = DBC.hub("select", ['name', 'deadline'])
        [logger.append({k: v}) for k, v in DBC_SELECT.items()]

        DBC_INSERT = DBC.hub("insert", "", ["cows", "loves", "food"])
        [logger.append({k: v}) for k, v in DBC_INSERT.items()]

        '''
            Still need to create a model system that inserts a table schema creation if not exist
        '''

        #  self.log saves entry to our file
        #  @ return [func, list]
        self.log['list'] = logger
        logs.info(self.log)

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP


        #  Data Harvesting
        #  -> Sites


if __name__ == "__main__":
    pass
