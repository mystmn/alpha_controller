import os
import sqlite3 as sql3


class DbController(object):
    def __init__(self, db_file=None, table=None):
        self.db = db_file
        self.table = table
        self.log = []

    def config(self):
        return {
            'db': self.db,
            'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
        }

    def connection_hub(self, table, var, selector="*"):
        self.validate_db_path()
        # create table if not exists TableName(col1 typ1, ..., colN typN)

        with sql3.connect(self.db) as conn:
            c = conn.cursor()

            if self.check_record_exist(c, table):

                if var == "select":
                    s = "SELECT "

                    if isinstance(selector, list):
                        s += "{s}".format(s=', '.join(selector))
                    else:
                        s += "{s}".format(s=selector)

                    s += " FROM {tn}".format(tn=table)

                    c.execute(s)
                    results = c.fetchall()
                    print(results)
            elif var == "insert":
                pass

            else:
                pass

        return self.log

    def check_record_exist(self, open_link, table):
        try:
            open_link.execute('SELECT 1 FROM {tn} LIMIT 1'.format(tn=table))
            open_link.fetchall()
            self.log.append("Confirmed data in query .table={}".format(table))
            return True

        except:
            self.log.append("Data is {}=None".format(table))
            return False

    def validate_db_path(self):

        if not os.path.exists(self.db):

            try:
                os.chdir(self.db)
                open(self.db, "w")
                self.validate_db_file()
                self.log.append("Created DB file {}".format(self.db))

            except:
                self.log.append("Unable to create db file {}".format(self.db))

        else:
            self.log.append("Confirmed file exist {}".format(self.db))
