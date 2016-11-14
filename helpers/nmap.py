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
        start, stop = 0, 4
        find_all = []
        by_six = []
        r = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)

        tc = r.communicate()  # tc = terminal communication

        splitting = tc[0].decode().split(" ")
        new = list(filter(None, splitting))

        cleansed_markers = self.position_word(new, "\n")

        with open("test.txt", "w", newline="\n") as f:
            f.write(str(tc[0].decode()))
            f.write("\nheader declared ={}\n\n".format(new[:stop]))

            i = 0
            s = []

            for each in cleansed_markers:
                print(each)
                for k, v in each.items():

                    if k <=3:
                        pass
                    else:
                        i += 1
                        s.append(v)
            f.write("{}".format(s))

            for i, each in enumerate(s):
                if i % 8 == 0:
                    f.write("{}".format(each))

                    f.write("{}".format("\n"))

                else:
                    f.write("{} \t".format(each))

            #  f.write(self.find_gate_way(tc[0].decode()))
            f.close()

        return find_all
        #  print(p[0][:search])
        #  print(pos.find("1:"))

    @staticmethod
    def position_word(per_lines=(), found=()):
        classy = {}
        rows = []
        i = 0

        for each_word in per_lines:

            i += 1

            if found in str(each_word):
                find_x = each_word.find("\n")

                before, after = each_word[:find_x], each_word[find_x + 1:]

                rows.append({i: before})
                i += 1
                rows.append({i: after})

            else:
                rows.append({i: each_word})

        return rows

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
