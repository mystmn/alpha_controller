def schema():
    return {
        'table_name': 'nmapScan',
        'fields': ('id', 'device', 'description', 'LastModifiedTime'),
        'id': 'INT',
        'device': 'CHARACTER(20) UNIQUE',
        'description': 'CHARACTER(75)',
        'LastModifiedTime': 'CURRENT_TIMESTAMP',
    }


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
