import os
import subprocess
from helpers import misc


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


class Terminal(object):
    @classmethod
    def is_method(cls):
        return cls.__name__

    @staticmethod
    def linux_subprocess(x=()):

        if x is ():
            error = Terminal.is_method() + ".linux"
            exit("No var set = {}...exiting".format(error))

        if len(x) <= 1:
            exit("Command needs to be a list")

        try:
            x = subprocess.Popen(x, stdout=subprocess.PIPE)

            return list(filter(None, x.communicate()[0].decode().split(" ")))

        except IOError as e:
            error = Terminal.is_method() + ".linux"
            exit("Major error occurred :: {} - {}".format(error, e))

    def filter_linux_route_n(x):
        '''
            Call $route -n
            Remove header range()...
            Create list with thread_results...
            find() row starts from \n and...
            :return set(list_exception_column)
        '''

        header_stop = 4
        row_start_pos = []
        row = 8
        exception_column = 1
        list_exception_column = []

        markers_dict = misc.search_replace_list(x, "\n")

        marker_list = misc.remove_range_append(markers_dict, header_stop)

        for num, each in enumerate(marker_list):
            if num % row == 0:
                if num >= row:  # No need to gather Row Header
                    row_start_pos.append(num + exception_column)

            for e in row_start_pos:
                if num == e:
                    list_exception_column.append(each)

        return set(list_exception_column)
