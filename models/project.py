class Engine(object):
    def __init__(self):
        self.schema = {
            'table_name': 'bobby',
            'fields': ['name', 'description', 'deadline'],
            'name': 'CHARACTER(20) UNIQUE',
            'description': 'CHARACTER(75)',
            'deadline': 'CHARACTER(20)',
        }
        self.x = ['PRIMARY KEY', 'UNIQUE']
        self.types = ['INT', 'CHARACTER(20)', 'TEXT', 'BLOB', 'REAL', 'NUMERIC']

    def db_schema(self):
        return self.schema


if __name__ == '__main__':
    f = Engine().db_schema()
    g = []

    for k, v in f.items():
        print("k={}".format(k))

        for h in f['fields']:
            if k == h:
                string = "{} {}".format(k, v)
                g.append(string)