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

    def connection_hub(self, var, name_columns, insert_values=""):
        self.validate_db_path()
        # create table if not exists TableName(col1 typ1, ..., colN typN)

        with sql3.connect(self.db) as conn:
            secure_conn = conn.cursor()

            if self.check_record_exist(secure_conn):  # Validate the requested table exist and there's one record

                if var == "select":
                    self.log.append(self.select_db(secure_conn, name_columns))

                elif var == "insert":
                    x, mes = self.insert_db(secure_conn, name_columns, insert_values)

                    if x:
                        self.log.append("Successful = {}".format(mes))
                        conn.commit()
                    else:
                        print("{}".format(mes))
                else:
                    self.log.append("Database did nothing")

        return self.log

    def insert_db(self, secure_conn, columns="", values=""):

        if not len(columns) is len(values):
            self.log.append("len(Columns) != len(values) for {}".format(self.table))
            return False

        try:
            s = "INSERT INTO {tn} (".format(tn=self.table)
            g, k = "", ""

            for x in columns:
                g += "{},".format(x)

            s += g[:-1] + ") VALUES ("

            for v in values:
                k += "'{}',".format(v)

            s += k[:-1] + ")"
            secure_conn.execute(s)
            final = True, s

        except sql3.IntegrityError:
            final = False, "TABLE={} requires a UNIQUE VALUE NOT ({})".format(self.table, values)

        self.log.append(final)

        return final

    def select_db(self, secure_conn, name_columns="*"):
        s = "SELECT "

        if isinstance(name_columns, list):
            s += "{s}".format(s=', '.join(name_columns))
        else:
            s += "{s}".format(s=name_columns)

        s += " FROM {tn}".format(tn=self.table)

        secure_conn.execute(s)
        results = secure_conn.fetchall()
        return list(results)

    def check_record_exist(self, open_link):
        try:
            open_link.execute('SELECT 1 FROM {tn} LIMIT 1'.format(tn=self.table))
            open_link.fetchall()
            self.log.append("Confirmed data in query .table={}".format(self.table))
            return True

        except:
            self.log.append("Data is {}=None".format(self.table))
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
