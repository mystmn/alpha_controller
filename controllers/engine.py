from helpers.menu import MainMenu as MM


class Main(object):
    def __init__(self):
        pass

    @staticmethod
    def start():
        number, command, message = MM().display()

        print("{} | {} | {}".format(number, command, message))

        #  Create a file log

        #  Commands to send out among the network to gather
        #  -> Models, Names, IP

        #  Data Harvesting
        #  -> Sites