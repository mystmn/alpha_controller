from helpers import cmd, menu, misc


def display_menu():
    return (
        {
            'mes': 'Would you like to run this automatically?',
            'reply': "Running automatically...sit back and relax",
            'com': ['route']
        },
        {
            'mes': 'Shall we run this manually?',
            'reply': 'You have a choice of options',
            'com': 'commands here',
        }
    )


def commands():
    return {
        'ping': "ping -c 2 ",
        'route': ['route', '-n'],
        'nmapOS': ['nmap', '-O' 'x']
    }


class NetworkScanner(object):
    black_list = [
        "0.0.0.0"
    ]

    log = {100: [], 200: [], 300: []}
    test = False

    def __init__(self):
        _name = type(self).__name__
        self.log[200].append("class __{} begins..".format(_name))

    def central_hub(self):
        terminal_executed = self.pull_terminal_options()

        done = self.return_gateway_sources(terminal_executed)

        exit(done)

        return self.dict_clean_none(self.log), done

    @staticmethod
    def pull_terminal_options():
        res = {}

        [res.update(each) for each in menu.nmap_initiate_menu(display_menu())]

        _user = res[int(misc.user_input_need_int(res))]

        for k, v in res.items():
            pass

        p = commands()
        for each in p:
            print(each)
        exit()

        _func = getattr(cmd.Terminal, "linux")

        executed_commands = _func(_user)

        return executed_commands[1]

    def return_gateway_sources(self, results):

        find_valid_gateways = misc.filter_command_route_n(results)

        minor_gateways = misc.blacklist_list_from_list(self.black_list, find_valid_gateways)

        completed = list(filter(None, minor_gateways))

        return completed

    @staticmethod
    def dict_clean_none(x):
        filter_log = {}

        for k, v in x.items():
            if v:
                filter_log[k] = v

        return filter_log


if __name__ == "__main__":
    pass
