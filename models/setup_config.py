import model, os
import sqlite3 as sql3


class DbController(object):
    def __init__(self, db_file=None, table=None, col=None, limit='20'):
        self.db = db_file
        self.table = table
        self.col = ['name', 'description']
        self.limit = limit

    @staticmethod
    def config():
        return {
            'db': model.config()['Model'],
            'desc': 'ORDER BY {} DESC'.format('id'),  # SELECT * FROM tablename ORDER BY column DESC LIMIT 1;
        }

    def test_creation_table(self):

        # 'Create TABLE bob (rowid INTEGER PRIMARY KEY, devices TEXT CHAR (50) NOT NULL)'
        # SELECT `type` FROM `cats`
        # sqlite3 mydatabase.db < db.schema
        try:
            con = sql3.connect(self.config()['db'] + self.db)

            print(",".join(self.col))

            con.cursor().execute('INSERT INTO {}({},{}) VALUES (?,?)'.format(self.table, 'name', 'description'),
                                 ("iron manss", "Gogogog!")
                                 )
            con.commit()
            con.close()
            return "Inserted data successful"

        except:
            return "Failed Migration"

            # cursor = con.cursor().execute('SELECT `name` FROM `{}` '.format('project'))
            # print(cursor.fetchall())
            # con.close()

    def test_insert_data(self):
        con = sql3.connect(self.config()['db'] + self.db)
        cursor = con.cursor().execute("INSERT INTO {}({},{},{},{}, {}) VALUES (?,?,?,?,? )" \
                                      .format(self.table, sc[0], sc[1], sc[2], sc[3], sc[4]), (a, b, c, d, e)
                                      )
        con.commit()
        con.close()

    def table_confirm_exist(self, loop=False):

        # print(self.config()['db'])
        # print(os.path.exists(self.config()['db'] + self.db))

        if not os.path.exists(self.config()['db'] + self.db):

            if not loop:
                try:
                    os.chdir(self.config()['db'])
                    open(self.db, "w")

                except:
                    return False

                return self.table_confirm_exist(True)

            return False

        else:
            return True

    def table_creation(self):

        try:
            with sql3.connect(self.config()['db'] + self.db) as con:
                con.cur().execute('CREATE TABLE {} (' \
                                  'rowid INTEGER PRIMARY KEY, ' \
                                  '{} TEXT CHAR(50) NOT NULL, ' \
                                  '{} TEXT CHAR(50), ' \
                                  '{} TEXT CHAR(50), ' \
                                  '{} TEXT CHAR(50), ' \
                                  '{} CURRENT_TIMESTAMP' \
                                  ')'.format(self.table, "bob", "rose", "mary", "cars"))
                con.commit()
                con.close()
            return [True, "Created Table"]
        except:
            return [False, "Table wasn't created, it may already exist"]


'''
    def table_insert(self, a="", b="", c="", d="", e=""):
        sc = self.config()['c']

        with sql3.connect(self.config()['db']) as con:
            con.cursor().execute("INSERT INTO {}({},{},{},{}, {}) VALUES (?,?,?,?,? )" \
                                 .format(self.table, sc[0], sc[1], sc[2], sc[3], sc[4]), (a, b, c, d, e))
            con.commit()
        con.close()
        return [True, "Data Inserted, {}, {}, {},{}".format(a, b, c, d)]

    def table_select(self, params=(), limit=()):
        s = "SELECT "
        n = "LIMIT "

        with sql.connect(self.config()['db']) as con:
            cur = con.cursor()

            if params == ():
                # result = cur.execute("SELECT * FROM {}".format(TABLE, limit))
                s += "* FROM "
            else:
                s += "{} FROM ".format(params)

            if limit == ():
                s += "{} {}".format(str(self.table), n + str(self.config()['limit']))
            else:
                s += "{} {}".format(str(self.table), n + str(limit))

            result = cur.execute(s).fetchall()

        con.close()
        return result
'''
