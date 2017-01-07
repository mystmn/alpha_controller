import random
from config import Core
from helpers import logs, menu, misc
from models.db import config
from helpers.nmap import NetworkScanner


class NetScan(object):
    @staticmethod
    def get_name():
        return __class__.__name__


class Main(object):
    def __init__(self):
        self.core_files = Core().get_directories()

    @staticmethod
    def project_tags():
        core_files = Core().get_directories()
        print(core_files['tag']['ProjectName'])
        print(core_files['tag']['ProjectPurpose'])
        print(core_files['Model'])

    def start(self):
        '''
            Display Menu Options
        '''
        NS = NetworkScanner()

        r = getattr(NS, "central_hub")

        network_log, results = r()

        logs.Scribe(dict, network_log)

        _tables = self.dynamic_db_connection()

        class_name = NetScan.get_name()

        name = "cocsws{}".format(random.randrange(100, 999999))
        _tables[class_name].db_insert([name, "location : WB227"])
        _tables[class_name].db_termination()
        logs.Scribe(dict, _tables[class_name].journal_logs())

        ''''
        name = "cocsws{}".format(random.randrange(100, 999999))
        model_results.db_insert([name, "location : WB227"])
        logs.Scribe(dict, model_results.journal_logs())
        '''

        # NSC.db_termination()

    def dynamic_db_connection(self):
        model_results = {}

        '''
            Accessing DB
        '''
        confirmed_models = self.scrap_model_folder()
        [logs.Scribe(dict, {200: "model keys logged ... {}".format(k)}) for k in confirmed_models.keys()]

        for k, v in confirmed_models.items():
            model_results[k] = config.Tunnel(self.core_files['DB'], confirmed_models, k)

        return model_results

    def scrap_model_folder(self):
        establish_connection = {}

        model_tags = [self.scrape(x) for x in misc.read_folder_files(self.core_files['Model'], "py")]

        for each in model_tags:
            for k, v in each.items():
                establish_connection[k] = v.schema()

        return establish_connection

    @staticmethod
    def scrape(name):
        g = {}
        names = "models." + name
        g[name] = __import__(names, fromlist=[''])
        return g


if __name__ == "__main__":
    pass

else:
    Main().project_tags()
    Main().start()
