import os  # http://stackabuse.com/python-check-if-a-file-or-directory-exists/
import inspect
from helpers import cmd

cmd.clear()

cl_setup = {
    'ProjectName': "** Project Master Blaster has begun ** ",
    'ProjectPurpose': "** This script was created to scan a network for information **",
    'Schedule': False,
    'Menu': False,
    'Logs': True,
    'Model': r'{}{}'.format(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')), "/models1/"),
    'Root': r'{}{}'.format(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '')), "/"),
}


#  Verify the needed directory exist
def dir_checker(x):
    IS = inspect.stack()

    if type(x) is list:
        for each_dir in x:

            if each_dir in cl_setup:
                try:
                    if not os.path.isdir(cl_setup[each_dir]):
                        print("Doesn't exist = {}".format(cl_setup[each_dir]))
                        print("fpath={}, func={}".format(IS[0][1], IS[0][3]))

                except IOError as e:
                    errno, strerror = e.args
                    print("{} doesn't exist".format(errno))
            else:
                var = "Doesn't exist = {}".format(str(each_dir))
                exit(var)

    elif type(x) is str:
        if not os.path.isdir(x):
            print("{} = broken".format(x))
    else:
        pass

dir_checker(['Model', 'Root', 'Controller'])


if __name__ == '__main__':
    print("test test")
