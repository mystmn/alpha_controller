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
            exit("No var set = {}".format(error))

        x = subprocess.Popen(x, stdout=subprocess.PIPE)

        return x.communicate()

    @staticmethod
    def decode(x):
        return list(filter(None, x[0].decode().split(" ")))
