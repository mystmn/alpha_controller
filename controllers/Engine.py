import random
from config import core
from helpers import logs, menu, misc
from models.db import config
from helpers.nmap import NetworkScanner as NS


class Main(object):
    def __init__(self):
        self.core_files = core().valid_paths()

    def start(self):
        logger = []

        print(self.core_files['tag']['ProjectName'])
        print(self.core_files['tag']['ProjectPurpose'])
        print(self.core_files['Model'])

        '''
            Display Menu Options
        '''
        network_log, results = NS().central_hub()
        logs.Scribe(dict, network_log)

        '''
            Accessing DB
        '''
        model_conn = self.scrap_model_folder()
        logs.Scribe(dict, {100: ["..again schema connection.."]})
        exit()

        #NSC = config.Tunnel(self.core_files['DB'], dict(model_conn['net_scan']))

        name = "cocsws{}".format(random.randrange(100, 999999))
        #NSC.db_insert([name, "lcation : WB227"])
        #logs.Scribe(dict, NSC.journal_logs())

        #NSC.db_termination()

    def scrap_model_folder(self):
        establish_connectioned = {}

        model_tags = [self.scrape(x) for x in misc.read_folder_files(self.core_files['Model'], "py")]

        for each in model_tags:
                for k, v in each.items():
                    establish_connectioned[k] = v.schema()

        return establish_connectioned

    @staticmethod
    def scrape(name):
        g = {}
        namey = "models." + name
        g[name] = __import__(namey, fromlist=[''])
        return g












        '''
        models running :: project, net_scan
        '''
        # MEC = main_engine.Controller(self.db, project.schema())

        # MEC.db_select(['name', 'deadline'])

        # MEC.db_insert(["Subs", "pies", "best food around"])

        # MEC.db_termination()

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP

        #  Data Harvesting
        #  -> Sites

if __name__ == "__main__":
    pass

else:
    Main().start()
