import random
from config import core
from helpers import logs, menu, misc
from models.db import config
from helpers.nmap import NetworkScanner as NS
#  from models import project, main_engine, net_scan
import models


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

        #  s = getattr(models.Defend, "schema")
        s = [self.scrape(x) for x in misc.read_folder_files(self.core_files['Model'], "py")]
        r = {}

        for e in s:
            for k, v in e.items():
                r[k] = v.schema()

        exit(r)

        NSC = config.Tunnel(self.core_files['DB'] + "main.db", s())

        name = "cocsws{}".format(random.randrange(100, 999999))
        NSC.db_insert([name, "location : WB227"])
        logs.Scribe(dict, NSC.journal_logs())

        NSC.db_termination()

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
