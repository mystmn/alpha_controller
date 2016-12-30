import os, errno
import sqlite3 as sql3


class Tunnel(object):
    def __init__(self, db_file=None, model_schema=None, model_name=None):
        ''' App Mandatory Start '''
        self.self_name = type(self).__name__
        self.log = {100: [], 200: [], 300: []}
        self.test = False
        ''' App Mandatory End '''

        self.db = db_file + "master.db"
        self.name = model_schema[model_name]
        self.blacklist = self.name['filter-out']

        self.schema = self.name['schema']
        self.table = self.schema['table_name']
        self.fields = self.schema['fields']
        ''' Mandatory Functions'''
        self.validate_db_path()

    def journal_logs(self):
        return self.log

    def db_connection(self):
        return sql3.connect(self.db)

    def db_termination(self):
        self.log[200].append("..db connection terminated")
        return self.db_connection().close()

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
            self.log[200].append("SUCCESS" + returns + "{}".format(results))
            return list(results)

        except sql3.OperationalError as e:
            self.log[100].append("FAILURE" + returns + "{}".format(e))

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

            print(s)
            conn.execute(s)
            conn.commit()
            self.log[200].append("SUCCESS" + returns + "{}".format(s))

        except sql3.IntegrityError as e:
            self.log[100].append("FAILURE" + returns + "{}".format(e))

    def validate_db_path(self):
        returns = "::db_path=\'{}\' exist already".format(self.db)

        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

        try:
            creation = sql3.connect(r"{}".format(self.db))
            file_handle = os.open(self.db, flags)
            self.log[200].append("DB file was created {} {}".format(self.db, returns))

        except OSError as e:
            if e.errno == errno.EEXIST:  # Failed as the file already exists.
                self.log[200].append("File already exist" + returns)

                self.create_table()
                pass
            else:  # Something unexpected went wrong so reraise the exception.
                self.log[100].append("FAILURE in db_file creation" + " :: {}".format(e))

    def create_table(self):
        returns = "::table=\'{}\' has been validated or created".format(self.table)
        columns = []

        #  Sort via the order of list(fields)
        for each_field in self.fields:
            for k, v in self.schema.items():
                if k == each_field:
                    columns.append("{} {}".format(k, v))

        try:
            x = "CREATE TABLE IF NOT EXISTS {tb} ({col})".format(tb=self.table, col=', '.join(columns))
            self.db_connection().execute(x)
            self.log[200].append("SUCCESS" + returns)

        except:
            self.log[100].append("FAILURE" + returns)
            exit("Need to add error catcher 'create_table'")

    def check_record_exist_in_table(self):
        returns = ":: DATA exist for table=\'{}\'".format(self.table)
        conn = self.db_connection().cursor()

        try:
            conn.execute('SELECT 1 FROM {tn} LIMIT 1'.format(tn=self.table))
            conn.fetchall()
            self.log[200].append("SUCCESS" + returns)

        except:
            self.log[100].append("FAILURE" + returns)
