import os, multiprocessing.dummy
import helpers.misc as misc
from helpers.cmd import Terminal, clear


class NetworkScanner(object):
    @staticmethod
    def multi_proc_ping(x=()):
        '''
            Uses OS.System to ping a count of 2
            :return string(list_r)
        '''
        list_r = []

        response = os.system("ping -c 2 " + x)

        if not bool(response):
            list_r.append(x)

        return str(list_r)

    def route_gateway(self, test=False):
        f_name = "nmap.txt"
        f_permissions = "w"

        '''
        :var test

        :return list(cleaner_results)

        :raises None
        '''

        tc = Terminal.linux(['route', '-n'])

        td = Terminal.decode(tc)

        rl = self.route_layout(td)

        cores = self.route_gateway_count()

        thread_results = cores.map(self.multi_proc_ping, [blank for blank in rl])

        clear()

        route_gateway_done = list(filter(None, thread_results))

        if test:
            with open(f_name, f_permissions, newline="\n") as f:
                f.write("{}".format(route_gateway_done))

            f.close()

        return route_gateway_done

    @staticmethod
    def route_gateway_count():

        core_count = 4 * multiprocessing.cpu_count()

        return multiprocessing.dummy.Pool(core_count)

    @staticmethod
    def route_layout(x):
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

    print(NS.route_gateway(True))
