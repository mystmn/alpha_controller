import os
import subprocess


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


class Terminal(object):
    @classmethod
    def is_method(cls):
        return cls.__name__

    @staticmethod
    def linux(x=()):

        if x is ():
            error = Terminal.is_method() + ".linux"
            exit("No var set = {}...exiting".format(error))

        if len(x) <= 1:
            exit("Command needs to be a list")

        try:
            x = subprocess.Popen(x, stdout=subprocess.PIPE)

            return True, list(filter(None, x.communicate()[0].decode().split(" ")))

        except IOError as e:
            error = Terminal.is_method() + ".linux"
            exit("Major error occurred :: {} - {}".format(error, e))
