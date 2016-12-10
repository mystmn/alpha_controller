import os
import sqlite3 as sql3


class Controller(object):
    def __init__(self, db_file=None, model_schema=None):
        self.db = db_file
        self.model = model_schema['schema']
        self.table = self.model['table_name']
        self.fields = self.model['fields']
        self.blacklist = model_schema['filter-out']
        self.log = []

        ''' Mandatory Functions'''
        self.validate_db_path()

    def db_connection(self):
        return sql3.connect(self.db)

    def db_termination(self):
        self.log.append("..db connection terminated")
        return self.db_connection().close()

    def journal_logs(self):
        return self.log

    def db_select(self, col_name):
        returns = ":: data selected = "
        conn = self.db_connection().cursor()

        self.check_record_exist_in_table()

        s = "SELECT "

        if isinstance(col_name, list):
            s += "{s}".format(s=', '.join(col_name))
        else:
            s += "{s}".format(s=col_name)

        s += " FROM {tn}".format(tn=self.table)

        try:
            conn.execute(s)
            results = conn.fetchall()
            self.db_termination()
            self.log.append("SUCCESS" + returns + "{}".format(results))
            return list(results)

        except sql3.OperationalError as e:
            self.log.append("FAILURE" + returns + "{}".format(e))

    def db_insert(self, values):
        returns = ":: data inserted = "
        conn = self.db_connection()

        try:
            s = "INSERT INTO {tn} (".format(tn=self.table)
            g, k = "", ""

            for x in self.fields:
                if x not in self.blacklist:
                    g += "{},".format(x)

            s += g[:-1] + ") VALUES ("

            for v in values:
                k += "'{}',".format(v)

            s += k[:-1] + ")"

            conn.execute(s)
            conn.commit()
            self.log.append("SUCCESS" + returns + "{}".format(s))

        except sql3.IntegrityError as e:
            self.log.append("FAILURE" + returns + "{}".format(e))

    def validate_db_path(self):
        returns = "::db_path=\'{}\' exist already".format(self.db)

        if not os.path.exists(self.db):

            try:
                os.chdir(self.db)
                open(self.db, "w")
                self.validate_db_file()
                self.log.append("SUCCESS" + returns)
                self.validate_db_path()

            except sql3.OperationalError as e:
                self.log.append("FAILURE" + " :: {}".format(e))

        else:
            self.log.append("SUCCESS" + returns)

            self.create_table()

    def create_table(self):
        returns = "::table=\'{}\' has been created".format(self.table)
        columns = []

        #  Sort via the order of list(fields)
        for h in self.fields:
            for k, v in self.model.items():
                if k == h:
                    string = "{} {}".format(k, v)
                    columns.append(string)

        try:
            x = "CREATE TABLE IF NOT EXISTS {tb} ({col})".format(tb=self.table, col=', '.join(columns))
            self.db_connection().execute(x)
            self.log.append("SUCCESS" + returns)

        except:
            self.log.append("FAILURE" + returns)
            exit("Need to add error catcher 'create_table'")

    def check_record_exist_in_table(self):
        returns = ":: DATA exist for table=\'{}\'".format(self.table)
        conn = self.db_connection().cursor()

        try:
            conn.execute('SELECT 1 FROM {tn} LIMIT 1'.format(tn=self.table))
            conn.fetchall()
            self.log.append("SUCCESS" + returns)

        except:
            self.log.append("FAILURE" + returns)
