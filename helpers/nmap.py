from helpers import cmd, menu, misc


def _display_menu():
    return (
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


def compare_option_viable(res):
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


class MenuPullCommands(object):
    black_list = [
        "0.0.0.0"
    ]

    log = {100: [], 200: [], 300: []}
    test = False

    commands = {
        'ping': "ping -c 2 ",
    }

    file = {
        'name': "nmap.txt",
        'permission': 'w',
    }

    def __init__(self):
        _name = type(self).__name__
        self.log[200].append("class __{} begins..".format(_name))

    def hub(self):
        res = {}

        [res.update(each) for each in menu.print_options(_display_menu())]

        _user = res[int(compare_option_viable(res))]

        terminal_executed = self.execute_terminal(_user)

        done = self.return_gateway_sources(terminal_executed)

        return self.dict_clean_none(self.log), done

    @staticmethod
    def execute_terminal(_user):

        executed_commands = cmd.Terminal.linux(_user)

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
