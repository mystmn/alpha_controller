from helpers import menu


def execute():
    menu_picked = getattr(menu.DynamicComparative(), "menu_pick")

    helper_nmap = menu_picked(self())

    helper_nmap['black_list'] = self()['black_list']

    '''
        needs to be in order
        provide executes and filters
        depend on executing dependencies
    '''
    #  r = [
    #      {'execute': {'route': 'X'}, {'ping': 'X'}},
    #      {'filters': 'route'}]

    new = {}
    i = 0
    for each in helper_nmap['execute']:

        i += 1

        if each in commands():

            new[i] = ({'exe': commands()[each]})

            if each in filters():
                new[i].update({'fi': filters()[each]})

    return new


def self():
    x = dict()

    x['_display_menu'] = (
        {
            'mes': 'Would you like to run this automatically?',
            'reply': "Running automatically...sit back and relax",
            'com': {
                #  maintain the order of execution
                'execute': ('route', 'ping'),
                'filter': ('route', None)
            },
        },
        {
            'mes': 'Shall we run this manually?',
            'reply': 'You have a choice of options',
            'com': [None, None]
        }
    )

    x['black_list'] = ["0.0.0.0"]

    return x


def commands():
    return ({
        'route': ['route', '-n'],
        'ping': ["ping", '{}', "-c", "2"],
        'nmapOS': ['nmap', '-O' 'x']
    })


def filters():
    return {
        'route': 'filter_linux_route_n'
    }


class Search(object):
    @staticmethod
    def hub():
        pass


if __name__ == "__main__":
    pass
