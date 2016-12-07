import sqlite3 as sql3


class DBController(object):
    def __init__(self, db_file=None, model_schema=None):
        self.model = model_schema
        self.db_file = db_file

        self.var = {
            'Insert': 'a',
            'Select': 'b',
            'Classes': 'c',
        }

    def __getattr__(self, item):
        try:
            if self.var[item] == 'Insert':
                print("Name was found")

            elif self.var[item] == 'Select':
                print("Selected was optional")
            else:
                print("Epic Failure")
        except:
            pass

    def sql_conn(self):
        with sql3.connect(self.db_file) as conn:
            return conn.cursor()

    def Select(self, x):
        self.sql_conn()
        print(x)

    def query_db(self):
        pass


if __name__ == '__main__':
    DBC = DBController("DB_file")
    DBC.Select(["passing"])
