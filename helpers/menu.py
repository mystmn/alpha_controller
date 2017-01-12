class DynamicComparative(object):
    def hub(self, _display_menu):
        res = {}

        dict_waiting = list(self.execute_pick_menu(_display_menu))

        [res.update(each) for each in dict_waiting]

        result = self.is_user_pick_optional(res)

        return res[result]

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
