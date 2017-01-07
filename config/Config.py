import os  # http://stackabuse.com/python-check-if-a-file-or-directory-exists/
import inspect


def project_tags():
    core_files = Core().get_directories()
    print(core_files['tag']['ProjectName'])
    print(core_files['tag']['ProjectPurpose'])
    print(core_files['Model'])


#  Check List
class Core(object):
    @staticmethod
    def get_path_structure():
        return {
            'tag':
                {
                    'ProjectName': "** Project Master Blaster has begun ** ",
                    'ProjectPurpose': "** This script was created to scan a network for information **",
                    'Schedule': False,
                    'Menu': False,
                    'Logs': True,
                },
            'structure':
                {
                    'Model': "/models/",
                    'DB': "/models/db/",
                    'Controller': "/controllers/",
                    'Root': "/",
                }
        }

    @staticmethod
    def path_join(key, value):

        parent_directory = os.path.join(os.path.dirname(__file__), '..', '')

        return {'{}'.format(key): r'{}{}'.format(parent_directory, value)}

    # Verify the needed directory exist
    def get_directories(self):
        IS = inspect
        x = {}

        for k, v in self.get_path_structure()['structure'].items():
            validated_dir = self.path_join(k, v)

            try:
                if not os.path.isdir(validated_dir[k]):
                    exit("Error :: path not found :: fpath={}, func={}".format(IS[0][1], IS[0][3]))
                else:
                    x.update({k: validated_dir[k]})
            except:
                exit("{} doesn't exist".format())

        x['tag'] = self.get_path_structure()['tag']

        #  print("{} == {}".format(validated_dir[k], msg))
        return x


if __name__ == '__main__':
    pass
