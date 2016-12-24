import os
import subprocess


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


class Terminal(object):

    @classmethod
    def is_method(cls):
        return cls.__name__

    def linux(self, x=()):

        #  exit("No var set = {} linux ...exiting".format(Terminal.is_method()) if x is () else '')

        #  exit("Command needs to be a list" if len(x) <= 1 else '')

        if x is ():
            error = Terminal.is_method() + ".linux"
            exit("No var set = {}...exiting".format(error))

        if len(x) <= 1:
            exit("Command needs to be a list")

        try:
            x = subprocess.Popen(x, stdout=subprocess.PIPE)

            return True, self.decoder(x.communicate())

        except IOError as e:
            error = Terminal.is_method() + ".linux"
            return False, "Major error occurred :: {} - {}".format(error, e)

    @staticmethod
    def decoder(x):
        return list(filter(None, x[0].decode().split(" ")))
