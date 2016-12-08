def schema():
    db = dict()
    #  Keep in mind [fields] creates the columns based on order of list()
    db['schema'] = {
                       'table_name': 'nmap',
                       'fields': ('id', 'device', 'description', 'LastModifiedTime'),
                       'id': 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL',
                       'device': 'CHARACTER(20)',
                       'description': 'CHARACTER(75)',
                       'LastModifiedTime': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL',
                   }
    db['filter-out'] = ['id', 'LastModifiedTime']
    return db


#  self.x = ['PRIMARY KEY', 'UNIQUE']
#  self.types = ['INT', 'CHARACTER(20)', 'TEXT', 'BLOB', 'REAL', 'NUMERIC']

if __name__ == '__main__':
    f = schema()
    g = []

    for k, v in f.items():
        print("k={}".format(k))

        for h in f['fields']:
            if k == h:
                string = "{} {}".format(k, v)
                g.append(string)
