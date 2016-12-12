def display_options(dictionary_with_list=""):
    dal = dictionary_with_list
    i = 0
    x = []

    if isinstance(dal, dict):
        warning = ["Please pick from the following"]
        [print("{}".format(dal)) for dal in warning]

        for k, v in dal.items():
            i += 1
            x.append({i: v['com']})
            print("{}) {}".format(int(i), v['mes']))

        return x

    else:
        exit("The menu list needs to be dict()[list]")