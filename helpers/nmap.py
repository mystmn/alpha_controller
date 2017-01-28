from helpers.menu import DynamicComparative


class Execute(object):
    def secure(self):

        menu_comparative = getattr(DynamicComparative(), "menu_pick")

        v = self._menu()

        menu_commands = menu_comparative(v)
        #    print("main var == {}".format(menu_commands))

        p = []
        i = 0
        for module_name in menu_commands['execute']:
            i += 1

            if module_name in self.commands().keys():
                _request = self.commands()[module_name]
                try:
                    _func = getattr(self, module_name)
                except:
                    exit("Unable to associate _func")

                p.append({i: _func(_request)})

        print(p)
        exit()

    @staticmethod
    def commands():
        return ({
            'route_gateway': ['route', '-n'],
            'nmapOS': ['nmap', '-O' 'x']
        })

    @staticmethod
    def filters():
        return ({
            'route': 'filter_linux_route_n'
        })

    @staticmethod
    def _menu():
        x = dict()

        x['_display_menu'] = (
            {
                'mes': 'Would you like to run this automatically?',
                'reply': "Running automatically...sit back and relax",
                'com': {
                    #  maintain the order of execution
                    'execute': ['route_gateway'],
                    'filter': ['route_gateway']
                },
            },
            {
                'mes': 'Shall we run this manually?',
                'reply': 'You have a choice of options',
                'com': [None, None]
            }
        )

        return x

    @staticmethod
    def terminal(x, y):
        import helpers.cmd as c
        _func = getattr(c.Terminal, x)

        return _func(y)

    def ping(self, x, _blacklist=None):
        if _blacklist is None:
            _blacklist = ["0.0.0.0"]

        ping_hostup = self.terminal('confirm_host_up', [x, _blacklist])

        return ping_hostup

    def route_gateway(self, x=None):
        route_process = self.terminal('linux_subprocess', x)

        route_filtered = self.terminal('filter_linux_route_n', route_process)

        route_completed = self.ping(route_filtered)

        return route_completed


if __name__ == "__main__":
    pass
