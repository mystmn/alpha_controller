import sys, os, glob


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

    #  if x in str([words for words in line]):

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
        #  [s.append(v) for k, v in each.items if not k <= num]
        [[s.append(v) for k, v in each.items() if not k <= num] for each in x]

    return list(s)


def convert_to_list(listing):
    a = []

    [a.append(x) for x in listing]

    return a


def blacklist_list_from_list(blacklist="", _set=""):
    a = []

    if isinstance(_set, set):
        [a.append(e) for e in _set if e not in blacklist]
        return list(a)

    exit("Requirements not met {} :: != list()".format(__name__, type(_set)))


def filter_command_route_n(x):
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

    markers_dict = search_replace_list(x, "\n")

    marker_list = remove_range_append(markers_dict, header_stop)

    for num, each in enumerate(marker_list):
        if num % row == 0:
            if num >= row:  # No need to gather Row Header
                row_start_pos.append(num + exception_column)

        for e in row_start_pos:
            if num == e:
                list_exception_column.append(each)

    return set(list_exception_column)


def read_folder_files(folder_path, pattern, black_list=["__init__"]):
    grab = glob.glob("{}*.{}".format(folder_path, pattern))
    dot = "."
    gather = []

    for x in grab:
        s = x.rindex('/') + 1
        g = x.replace(dot + pattern, "")

        if g[s:] not in black_list:
            gather.append(g[s:])

    return gather


def user_input_need_int(res):
    while True:
        mes = "try again.."
        _user = input("> ")

        if not _user.isdigit():
            mes += "'{}' needs to be an int()".format(_user)
            print(mes)
            continue

        elif _user not in str(res.keys()):
            mes += "'{}' isn\'t an available option".format(_user)
            print(mes)
            continue
        else:
            break

    return _user
