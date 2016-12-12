import random
from config.main import CL
from helpers import logs, menu
from helpers import nmap
from models import project, main_engine, net_scan


class Main(object):
    def __init__(self):
        #  helpers.logs.[info, debug, critical] RETURN ['func', 'message']
        self.log = {
            'func':
                __name__ + "_start",
            'list': [],
        }

        self.db = CL['Model'] + "main.db"

    def start(self):
        logger = []

        print(CL['ProjectName'])
        print(CL['ProjectPurpose'])
        print(CL['Model'])

        #  Only passes if completed.
        NSC = nmap.NetworkScanner()
        item_given = NSC.terminal_display()

        log, results = NSC.central_hub(item_given)

        logger.append(log)

        '''
        models running :: project, net_scan
        '''
        #MEC = main_engine.Controller(self.db, project.schema())

        #MEC.db_select(['name', 'deadline'])

        #MEC.db_insert(["Subs", "pies", "best food around"])

        #MEC.db_termination()

        #logger.append(MEC.journal_logs())

        NSC = main_engine.Controller(self.db, net_scan.schema())

        # logger.append(NSC.journal_logs())

        name = "cocsws{}".format(random.randrange(100, 999999))
        NSC.db_insert([name, "location : WB227"])
        logger.append(NSC.journal_logs())

        NSC.db_termination()

        # logger.append(NSC.journal_logs())

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
