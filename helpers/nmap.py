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
        find_all = []
        by_six = []
        r = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)

        tc = r.communicate()  # tc = terminal communication

        splitting = tc[0].decode().split(" ")
        new = list(filter(None, splitting))
        results = self.find_characters(new)

        with open("test.txt", "w", newline="\n") as f:
            f.write(str(results))
            #  f.write(self.find_gate_way(tc[0].decode()))
        f.close()

        p = tc[0].decode()
        s = "wlo1"
        r = "mtu"

        results = self.find_position_range(p, s, r)
        find_all.append("find={}, pos={}".format("both", results))

        return find_all
        #  print(p[0][:search])
        #  print(pos.find("1:"))

    def find_characters(self, lines=(), start=()):
        positioning = []
        for each_word in lines:

            if "\n" in str(each_word):
                positioning.append(each_word)

        return positioning




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
