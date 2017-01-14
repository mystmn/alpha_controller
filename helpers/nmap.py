from helpers import cmd, misc, menu


def _self():
    x = dict()

    x['_display_menu'] = (
        {
            'mes': 'Would you like to run this automatically?',
            'reply': "Running automatically...sit back and relax",
<<<<<<< HEAD
            'com': ['route']
=======
            'com': {
                'execute': ['route', '-n'],
                'helper': 'filter_linux_route_n'
            },
>>>>>>> a234a3e7f42d8d3817c4d0c5f6d127fac954a413
        },
        {
            'mes': 'Shall we run this manually?',
            'reply': 'You have a choice of options',
            'com': [None, None]
        }
    )

    x['black_list'] = ["0.0.0.0"]

<<<<<<< HEAD
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
=======
    x['log'] = {100: [], 200: [], 300: []}
    return x

>>>>>>> a234a3e7f42d8d3817c4d0c5f6d127fac954a413

class Search(object):
    @staticmethod
    def hub():
        self = _self()

        menu_pulled = getattr(menu.DynamicComparative(), "hub")

<<<<<<< HEAD
        _user = res[int(misc.user_input_need_int(res))]

        for k, v in res.items():
            pass

        p = commands()
        for each in p:
            print(each)
        exit()

        _func = getattr(cmd.Terminal, "linux")

        executed_commands = _func(_user)
=======
        app_processing = dict(menu_pulled(self["_display_menu"]))

        terminal = cmd.Terminal
>>>>>>> a234a3e7f42d8d3817c4d0c5f6d127fac954a413

        cmd_results = terminal.linux_subprocess(app_processing['execute'])

        find_terminal_filter = getattr(terminal, app_processing['helper'])

        filter_processed = find_terminal_filter(cmd_results)

        minor_gateways = misc.blacklist_list_to_list(self['black_list'], filter_processed)

        completed = list(filter(None, minor_gateways))

        return misc.dict_clean_none(self["log"]), completed


if __name__ == "__main__":
    pass
