import os, multiprocessing.dummy
import helpers.misc as misc
from helpers.cmd import Terminal, clear


class NetworkScanner(object):
    def __init__(self):
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
        self.log = []

    def central_hub(self, test=False):
        '''
        :var test

        :return list(cleaner_results)

        :raises None
        '''

        tc = Terminal.linux(['route', '-n'])
        self.log.append("...ran 'route -n' ...")

        rl = self.results_text_layout(Terminal.decode(tc))
        self.log.append("...filtered through the list...")

        cores = self.route_gateway_count()

        thread_results = cores.map(self.command_run, [blank for blank in rl])

        clear()

        route_gateway_done = list(filter(None, thread_results))

        if test:
            with open(self.file['name'], self.file['permission'], newline="\n") as f:
                f.write("{}".format(route_gateway_done))
                self.log.append("...list has been saved to file = {}".format(self.file['name']))

            f.close()

        return self.log, route_gateway_done

    def command_run(self, host_up_or_down=()):
        '''
            Uses OS.System to ping a count of 2
            :return string(list_r)
        '''
        if host_up_or_down not in self.black_list_connections:

            if not bool(os.system(self.commands['ping'] + host_up_or_down)):
                self.log.append("{} host is up".format(host_up_or_down))
                return str(host_up_or_down)

    @staticmethod
    def route_gateway_count():

        core_count = 4 * multiprocessing.cpu_count()

        return multiprocessing.dummy.Pool(core_count)

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

            for e in row_start_pos:

                if num == e:  # IS list[position] == exception_column + row
                    list_exception_column.append(each)

        return set(list_exception_column)


if __name__ == "__main__":
    NS = NetworkScanner()

    print(NS.central_hub(True))
