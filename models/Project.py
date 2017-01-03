def schema():
    db = dict()

    db['schema'] = {
        'table_name': 'project',
        'fields': ('name', 'description', 'deadline'),
        'name': 'CHARACTER(20) UNIQUE',
        'description': 'CHARACTER(75)',
        'deadline': 'CHARACTER(20)',
    }
    #  Blacklist item's that are automatised by SQLite3
    db['filter-out'] = []
    return db


#  self.x = ['PRIMARY KEY', 'UNIQUE']
#  self.types = ['INT', 'CHARACTER(20)', 'TEXT', 'BLOB', 'REAL', 'NUMERIC']

if __name__ == '__main__':
    pass
