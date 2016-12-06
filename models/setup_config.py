import os
import sqlite3 as sql3


class DbController(object):
    def __init__(self, db_file=None, model_schema=None):
        self.db = db_file
        self.model = model_schema
        self.table = model_schema['table_name']
        self.fields = model_schema['fields']
        self.log = []

    def hub(self, database_operator, name_columns="", insert_values=""):
        db_results = {}
        '''
        :param database_operator:
        :param name_columns:
        :param insert_values:
        :return self.log:
        '''

        self.validate_db_path()  # create database file if not exists

        with sql3.connect(self.db) as conn:
            secure_conn = conn.cursor()

            if self.check_record_exist_in_table(
                    secure_conn):  # Validate the requested table exist and there's one record

                if database_operator == "select":
                    db_results[database_operator] = self.select_db(secure_conn, name_columns)

                elif database_operator == "insert":
                    booleon, results = self.insert_db(secure_conn, insert_values)

                    if booleon:
                        conn.commit()
                        m = "SUCCESSFUL"
                    else:
                        m = "FAILED"

                    db_results[database_operator] = "{} :: {}".format(m, results)

                else:
                    db_results['operator_status'] = "NOT found. Leaving after accomplishing nothing"

            else:
                #  Table wasn't found. One needs to be created
                booleon, mes = self.create_table(secure_conn)

                if booleon:

                    db_results['table_creation'] = "Table was created :: {}".format(mes)
                else:
                    db_results['table_creation'] = "{}".format(mes)

        db_results['log'] = self.log

        return db_results

    def create_table(self, secure_conn):
        g = []

        for k, v in self.model.items():
            for h in self.fields:
                if k == h:
                    string = "{} {}".format(k, v)
                    g.append(string)

        try:
            x = "CREATE TABLE IF NOT EXISTS {tb} ({col})".format(tb=self.table, col=', '.join(g))
            secure_conn.execute(x)
            return True, x

        except:
            return False, "Error :: {} wasn't created".format(self.table)

    def insert_db(self, secure_conn, values=""):

        if not len(self.fields) is len(values):
            self.log.append("len(Columns) != len(values) for {}".format(self.table))
            return False, False

        try:
            s = "INSERT INTO {tn} (".format(tn=self.table)
            g, k = "", ""

            for x in self.fields:
                g += "{},".format(x)

            s += g[:-1] + ") VALUES ("

            for v in values:
                k += "'{}',".format(v)

            s += k[:-1] + ")"
            secure_conn.execute(s)
            final = True, s

        except sql3.IntegrityError as e:
            final = False, "TABLE={} requires a UNIQUE VALUE :: Error={}".format(self.table, e)

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

    def check_record_exist_in_table(self, open_link):
        self.log.append("Does the requested table exist...")
        try:
            open_link.execute('SELECT 1 FROM {tn} LIMIT 1'.format(tn=self.table))
            open_link.fetchall()

            self.log.append("...confirmed at least one record exist in 'table={}'".format(self.table))
            return True

        except:
            self.log.append("...no valid data exist '{}=None'".format(self.table))
            return False

    def validate_db_path(self):

        if not os.path.exists(self.db):

            try:
                self.log.append('attempting to create database=\'{}\''.format(self.db))
                os.chdir(self.db)
                open(self.db, "w")
                self.validate_db_file()
                self.log.append('creation of database=\'{}\' was SUCCESSFUL'.format(self.db))

            except:
                self.log.append('error occurred while attempting to create database=\'{}\''.format(self.db))

        else:
            self.log.append('database=\'{}\' has been validated'.format(self.db))

