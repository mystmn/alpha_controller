import subprocess
import os
import multiprocessing.dummy


class NetworkScanner(object):
    def __int__(self):
        self.white_list = ''
        self.black_list = ''
        self.string_formatter = 'nmap'

    '''
        Uses OS.System to ping a count of 2
        :return string(list_r)
    '''

    @staticmethod
    def multi_proc_ping(x=()):
        list_r = []

        response = os.system("ping -c 2 " + x)

        if not bool(response):
            list_r.append(x)

        return str(list_r)

    '''
        Multi treads ping and return results
        :return list(cleaner_results)
    '''

    def process(self):
        set_gateway_returns = self.terminal_route()

        core_count = 4 * multiprocessing.cpu_count()
        p = multiprocessing.dummy.Pool(core_count)

        results = p.map(self.multi_proc_ping, [x for x in set_gateway_returns])

        cleaner_results = list(filter(None, results))

        with open("test.txt", "w", newline="\n") as f:
            f.write("{}".format(cleaner_results))

        f.close()

        return cleaner_results

    '''
        Call $route -n
        Remove header range()...
        Create list with results...
        Find row starts from \n and...
        :return set(list_exception_column)
    '''

    def terminal_route(self):
        header_stop = 4
        row_start_pos = []
        row = 8
        exception_column = 1
        list_exception_column = []

        r = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)

        tc = r.communicate()  # tc = terminal communication

        present_as_list = list(filter(None, tc[0].decode().split(" ")))

        markers_dict = self.search_replace_list(present_as_list, "\n")

        #  [{i: value}, {i: value}...]
        #  returns [value, value...]
        marker_list = self.skip_header_and_re_list(markers_dict, header_stop)

        for num, each in enumerate(marker_list):

            if num % row == 0:  # find the row starting position

                if num >= row:  # No need to gather Row Header
                    row_start_pos.append(num + exception_column)

            for e in row_start_pos:

                if num == e:  # IS list[position] == exception_column + row
                    list_exception_column.append(each)

        return set(list_exception_column)

    ''' Take list, skip a range, and return list()
        :return list(s)
    '''

    @staticmethod
    def skip_header_and_re_list(x=(), num=()):
        s = []

        if isinstance(x, list):
            for each in x:
                for k, v in each.items():

                    if k <= num:  # Header is k[0:3]
                        pass
                    else:

                        s.append(v)
        else:
            pass

        return list(s)

    '''
        Find character and replace
        if character is combined within two strings it appends both
        to a list
        :return class {i: value}
    '''

    @staticmethod  # search for string, split word, and return list()
    def search_replace_list(line=(), x=()):
        new_line = []
        i = 0

        for words in line:
            i += 1

            if x in str(words):
                found_x = words.find(x)

                before, after = words[:found_x], words[found_x + 1:]

                new_line.append({i: before})

                i += 1
                new_line.append({i: after})

            else:
                new_line.append({i: words})

        return new_line

    @staticmethod
    def find_gate_way(listings=()):
        return listings.split()