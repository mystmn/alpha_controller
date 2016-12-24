import os  # http://stackabuse.com/python-check-if-a-file-or-directory-exists/
import inspect


#  Check List
class Core(object):
    @staticmethod
    def path_finder():
        x = {}
        x['tag'] = {
            'ProjectName': "** Project Master Blaster has begun ** ",
            'ProjectPurpose': "** This script was created to scan a network for information **",
            'Schedule': False,
            'Menu': False,
            'Logs': True,
        }
        x['structure'] = {
            'Model': "/models/",
            'Controller': "/controllers/",
            'Root': "/",
        }

        return x

    def path_join(self, key, value):

        parent_directory = os.path.join(os.path.dirname(__file__), '..', '')

        return {'{}'.format(key): r'{}{}'.format(parent_directory, value)}

    # Verify the needed directory exist
    def dir_checker(self):
        IS = inspect
        x = {}

        for k, v in self.path_finder()['structure'].items():
            validated_dir = self.path_join(k, v)

            try:
                if not os.path.isdir(validated_dir[k]):
                    exit("Error :: path not found :: fpath={}, func={}".format(IS[0][1], IS[0][3]))
                else:
                    x.update({k: validated_dir[k]})
            except:
                exit("{} doesn't exist".format())

        x['tag'] = self.path_finder()['tag']

        #  print("{} == {}".format(validated_dir[k], msg))
        return x

    def valid_paths(self):
        completed_list = self.dir_checker()
        return completed_list


if __name__ == '__main__':
    pass

