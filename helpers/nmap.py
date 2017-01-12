from helpers import cmd, misc, menu


def _self():
    x = dict()

    x['_display_menu'] = (
        {
            'mes': 'Would you like to run this automatically?',
            'reply': "Running automatically...sit back and relax",
            'com': {
                'execute': ['route', '-n'],
                'helper': 'filter_linux_route_n'
            },
        },
        {
            'mes': 'Shall we run this manually?',
            'reply': 'You have a choice of options',
            'com': [None, None]
        }
    )

    x['black_list'] = ["0.0.0.0"]

    x['log'] = {100: [], 200: [], 300: []}
    return x


class Search(object):
    @staticmethod
    def hub():
        self = _self()

        menu_pulled = getattr(menu.DynamicComparative(), "hub")

        app_processing = dict(menu_pulled(self["_display_menu"]))

        terminal = cmd.Terminal

        cmd_results = terminal.linux_subprocess(app_processing['execute'])

        find_terminal_filter = getattr(terminal, app_processing['helper'])

        filter_processed = find_terminal_filter(cmd_results)

        minor_gateways = misc.blacklist_list_to_list(self['black_list'], filter_processed)

        completed = list(filter(None, minor_gateways))

        return misc.dict_clean_none(self["log"]), completed


if __name__ == "__main__":
    pass
