def display_options(set_with_list=""):
    i = 0
    x = []
    warning = ["Please pick from the following"]

    if isinstance(set_with_list, tuple):

        [print("{}".format(dal)) for dal in warning]

        i = 0
        for each in set_with_list:
            i += 1
            print("{}) {}".format(int(i), each['mes']))
            x.append({i: each['com']})
        return x

    else:
        f = __file__
        exit("The menu list needs to be tuple()[list]")
