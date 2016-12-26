import random
from config import core
from helpers import logs, menu
from helpers import nmap
from models import project, main_engine, net_scan


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

        NSC = nmap.NetworkScanner()

        item_given = NSC.terminal_display()

        '''
            Return route -n results
        '''
        network_log, results = NSC.central_hub(item_given)
        logs.Scribe(dict, network_log)


        '''
            Accessing DB
        '''
        NSC = main_engine.Controller(self.core_files['Model'] + "main.db", net_scan.schema())

        name = "cocsws{}".format(random.randrange(100, 999999))
        NSC.db_insert([name, "location : WB227"])
        logger.append(NSC.journal_logs())

        NSC.db_termination()

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
