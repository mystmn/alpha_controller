

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
    #  Blacklist item's that are automatised by SQLite3
    db['filter-out'] = ['id', 'LastModifiedTime']
    return db

#  self.x = ['PRIMARY KEY', 'UNIQUE']
#  self.types = ['INT', 'CHARACTER(20)', 'TEXT', 'BLOB', 'REAL', 'NUMERIC']
