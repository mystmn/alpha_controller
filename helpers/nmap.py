import subprocess


class NetworkScanner(object):
    def __int__(self):
        self.white_list = ''
        self.black_list = ''
        self.string_formatter = 'nmap'

    @staticmethod
    def process():
        try:
            test = subprocess.Popen(["ping", "192.168.15.1", "-c", "3"], stdout=subprocess.PIPE)
            print(test.communicate())
        except:
            print("Not looking good")
# What's my list of segments?

# Then Throw the commands

# Save the results

# What to do with the results?
