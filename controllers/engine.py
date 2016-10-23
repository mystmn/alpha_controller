from helpers.menu import MainMenu as MM


class Main(object):
    def __init__(self):
        number, command, message = MM().display()

        print("{} | {} | {}".format(number, command, message))