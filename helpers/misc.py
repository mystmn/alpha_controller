import sys, os


def cur_function():
    return sys._getframe().f_code.co_name


def cur_file_path(x):
    return os.path.basename(x)


def search_replace_list(line, x):
    '''
        Find character and replace
        if character is combined within two strings it appends both
        to a list
        :return class {i: value}
    '''

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


def remove_range_append(x="", num=""):
    ''' Take list, skip a range, and return list()
        :return list(s)
    '''
    s = []

    if isinstance(x, list):
        for each in x:
            for k, v in each.items():

                if k <= num:  # Header is k[0:3]
                    pass
                else:
                    s.append(v)
    return list(s)


def convert_to_list(listing):
    a = []

    [a.append(x) for x in listing]

    return a


def filter_out_string(string, _set):
    a = []
    if isinstance(_set, set):
        for e in _set:
            if e not in string:
                a.append(e)

        return list(a)

    exit("Requirement :: {} != list()".format(type(_set)))
