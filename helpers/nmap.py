import os, threading
from helpers import cmd, menu, misc


class NetworkScanner(object):
    def __init__(self):
        self.log = []
        self.commands = {
            'ping': "ping -c 2 ",
        }

        self.file = {
            'name': "nmap.txt",
            'permission': 'w',
        }

        self.black_list_connections = [
            "0.0.0.0"
        ]

        self.menu = (
            {
                'mes': 'Would you like to run this automatically?',
                'reply': "Running automatically...sit back and relax",
                'com': ['route', '-n'],
            },
            {
                'mes': 'Shall we run this manually?',
                'reply': 'You have a choice of options',
                'com': 'commands here',
            }
        )

    def terminal_display(self, x=True, mes=""):
        res = {}
        user_input = ""

        if not x:
            cmd.clear()
            print(mes)
            self.log.append(mes)

        listed_options = menu.display_options(self.menu)

        try:
            user_input = int(input("> "))
            self.log.append("..asked the user what command to..")

        except:
            mes = " ** Answer needs to be an int.. **"
            self.log.append("error returning :: {}".format(mes))
            return self.terminal_display(False, mes)

        # Let's turn this sucker from a list to a dict
        [res.update(each) for each in listed_options]

        if user_input in res:
            return res[user_input]
        else:
            mes = " ** That choice isn't optional.. ** "

        return self.terminal_display(False, mes)

    def central_hub(self, command, test=False):
        '''
        :var test

        :return list(cleaner_results)

        :raises None
        '''

        boolean, results = cmd.Terminal().linux(command)

        if not boolean:
            self.log.append("False hope was placed in the terminal")
            exit(results)

        scrub_results = self.results_text_layout(results)

        cmd.clear()

        pressing = misc.filter_out_string(self.black_list_connections, scrub_results)

        route_gateway_done = list(filter(None, pressing))

        if test:
            self.log.append("...printing test results in :: {}".format(self.file['name']))

            with open(self.file['name'], self.file['permission'], newline="\n") as f:
                f.write("{}".format(route_gateway_done))
            f.close()

        return self.log, route_gateway_done

    @staticmethod
    def results_text_layout(x):
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

        #  [{i: value}, {i: value}...]
        #  returns [value, value...]
        marker_list = misc.remove_range_append(markers_dict, header_stop)

        for num, each in enumerate(marker_list):

            if num % row == 0:  # find the row starting position

                if num >= row:  # No need to gather Row Header
                    row_start_pos.append(num + exception_column)

            if [num == e for e in row_start_pos]:
                list_exception_column.append(each)

        return set(list_exception_column)


if __name__ == "__main__":
    NS = NetworkScanner()

    print(NS.central_hub(True))
