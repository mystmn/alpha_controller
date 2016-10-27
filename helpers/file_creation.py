import fileinput
from pathlib import Path

'''
f = ''

each_line = FeedList().start(f)

if not each_line:
    print("The requested file {} doesn't exist".format(f))

for each in each_line:
    print(FeedList().read_file('<sms', '/\"', 'address=\"', 'date', each), end='')
'''


class FileStructure(object):
    #  input(file path) return
    @staticmethod
    def start(x):
        if not Path(x).is_file():
            return False
        # Back up the original file
        return fileinput.FileInput(x, inplace=True, backup='.bak')

    @staticmethod
    def read_file():
        pass

if __name__ == '__main__':
    pass