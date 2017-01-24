from helpers.misc import isset_list


class DynamicComparative(object):
    @classmethod
    def is_method(cls):
        return cls.__name__

    def menu_pick(self, x):
        res = {}

        white_list = ['_display_menu']

        isset_list(self.is_method(), x, white_list)

        dict_waiting = list(self.execute_pick_menu(x['_display_menu']))

        [res.update(each) for each in dict_waiting]

        int_results = self.is_user_pick_optional(res)

        return res[int_results]

    @staticmethod
    def execute_pick_menu(set_with_list=""):
        i = 0
        x = []
        warning = ["Please pick from the following"]

        if isinstance(set_with_list, tuple):

            [print("{}".format(dal)) for dal in warning]

            i = 0
            for each in set_with_list:
                i += 1
                print("{}) {}".format(int(i), each['mes']))

                # approved values returned
                x.append({i: each['com']})
            return x

        else:
            f = __file__
            exit("The menu list needs to be tuple()[list]..{}".format(f))

    @staticmethod
    def is_user_pick_optional(res):
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

        return int(_user)
