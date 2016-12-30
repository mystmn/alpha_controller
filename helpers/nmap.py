from helpers import cmd, menu, misc


class NetworkScanner(object):
    def __init__(self):
        self.self_name = type(self).__name__
        self.log = {100: [], 200: [], 300: []}
        self.test = False

        self.commands = {
            'ping': "ping -c 2 ",
        }

        self.file = {
            'name': "nmap.txt",
            'permission': 'w',
        }

        self.black_list_connections = [
            "0.0.0.0"
        ]

        self.menu = (
            {
                'mes': 'Would you like to run this automatically?',
                'reply': "Running automatically...sit back and relax",
                'com': ['route', '-n'],
            },
            {
                'mes': 'Shall we run this manually?',
                'reply': 'You have a choice of options',
                'com': 'commands here',
            }
        )
        self.log[200].append("class __{} begins..".format(self.self_name))

    def is_error_message(self, x, mes):

        if not x:
            cmd.clear()
            print(mes)
            self.log[200].append(mes)

    def menu_listing(self):
        res = {}
        [res.update(each) for each in menu.display_options(self.menu)]
        return res

    def terminal_display(self):
        # Turn the sub.items() to a list for easy comparison
        dict_current = dict(self.menu_listing())

        _user = input("> ")

        #  Only accepts positive numbers

        if _user.isdigit():
            if _user in str(dict_current.keys()):
                return dict_current[int(_user)]
            else:
                cmd.clear()
                mes = "'{}' isn\'t an available option".format(_user)
                self.log[100].append(mes)
                print(mes)
                return self.terminal_display()
        else:
            cmd.clear()
            mes = "'{}' needs to be an int()".format(_user)
            self.log[100].append(mes)
            print(mes)
            return self.terminal_display()

    def central_hub(self):
        command = self.terminal_display()

        boolean, results = cmd.Terminal().linux(command)

        if not boolean:
            self.log[100].append("False hope was placed in the terminal")
            exit(results)

        scrub_results = misc.results_text_layout(results)

        cmd.clear()

        route_gateway_done = [list(filter(None, x)) for x in
                              misc.filter_out_string(self.black_list_connections, scrub_results)]

        if self.test:
            self.log[200].append("...printing test results in :: {}".format(self.file['name']))

            with open(self.file['name'], self.file['permission'], newline="\n") as f:
                f.write("{}".format(route_gateway_done))
            f.close()

        return self.remove_empty(self.log), route_gateway_done

    @staticmethod
    def remove_empty(x):
        filter_log = {}

        for k, v in x.items():
            if v:
                filter_log[k] = v

        return filter_log


if __name__ == "__main__":
    pass
