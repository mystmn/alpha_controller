import sys, os


def cur_function():
    return sys._getframe().f_code.co_name


def cur_file_path(x):
    return os.path.basename(x)
