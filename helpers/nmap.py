import subprocess


class NetworkScanner(object):
    def __int__(self):
        self.white_list = ''
        self.black_list = ''
        self.string_formatter = 'nmap'

    def process(self):
        s = self.whats_my_ip()
        '''
        segment = input("What's the segment?")

        try:
            test = subprocess.Popen(["ping", segment, "-c", "3"], stdout=subprocess.PIPE)
            print(test.communicate())

        except:
            print("Not looking good")
        '''
        return s

    def whats_my_ip(self):
        header_stop = 4
        row_start_pos = []
        row = 8
        col = 3
        
        r = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)

        tc = r.communicate()  # tc = terminal communication

        present_as_list = list(filter(None, tc[0].decode().split(" ")))

        markers_dict = self.search_replace_list(present_as_list, "\n")

        with open("test.txt", "w", newline="\n") as f:

            #  [{i: value}, {i: value}...]
            #  returns [value, value...]
            marker_list = self.skip_header_and_re_list(markers_dict, header_stop)

            for num, each in enumerate(marker_list):

                #  is this a starting row string
                if num % row == 0:  # find the row starting position
                    f.write("\n")

                    if num >= row:  # No need to gather Row Header
                        row_start_pos.append(num + col)

                for e in row_start_pos:
                    if num == e:  # IS list[position] == col + row
                        f.write("#{: >17}".format(each))

                #  If not a starting row string then print
                f.write("{: >17}".format(each))

            # f.write(self.find_gate_way(tc[0].decode()))
            f.close()

        #  print(p[0][:search])
        #  print(pos.find("1:"))

    #  Take list, skip a range, and re key
    #  @ x[0:3]
    @staticmethod
    def skip_header_and_re_list(x, num):
        i = 0
        s = []

        if isinstance(x, list):
            for each in x:
                for k, v in each.items():

                    if k <= num:  # Header is k[0:3]
                        pass
                    else:
                        i += 1
                        s.append(v)
        else:
            pass

        return s

    @staticmethod  # search for string, split word, and return list()
    def search_replace_list(line=(), char_search=()):
        new_line = []
        i = 0

        for words in line:

            i += 1

            if char_search in str(words):
                find_x = words.find(char_search)

                before, after = words[:find_x], words[find_x + 1:]

                new_line.append({i: before})
                i += 1
                new_line.append({i: after})

            else:
                new_line.append({i: words})

        return new_line

    def find_gate_way(self, listings=(), spacing=()):
        r = listings.split()
        return r

    def find_position_range(self, full_line=(), start=(), finish=()):

        try:
            count_finish = len(finish)

            start_position = full_line.find(start)
            second_position = full_line[start_position:].find(finish)

            added_positioning = start_position + second_position
        except:
            print("error")

        return full_line[start_position:added_positioning + count_finish]

# What's my list of segments?

# Then Throw the commands

# Save the results

# What to do with the results?
