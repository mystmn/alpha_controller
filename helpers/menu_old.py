from helpers import cmd


# NMB = menu selector
# MES = Message of display
# COM = command to be executed

class Display(object):

    def __init__(self):
        self.config = [
            {
                'NMB': 0,
                'MES': "Scan for all information",
                'COM': [
                    "jpg"
                ]
            },
            {
                'NMB': 1,
                'MES': "Dummy #1",
                'COM': [
                    "ex1",
                    "ex2",
                ]
            },
            {
                'NMB': 2,
                'MES': "Dummy #2",
                'COM': "..and here we go!"
            }
        ]

    #  return menu[int(NMB), str(MSG), str(COM)]
    def welcome(self, error=()):
        if error is not ():
            cmd.clear()
            print("error = {}\n".format(error))

        else:
            # Display a one time HEADER
            self.header()

        menu_range = self.print_set(self.config)

        validation, user_result = self.choice()

        if validation:
            #  Is the user_result even optional
            if user_result in menu_range:
                mu = self.config[user_result]
                return mu['NMB'], mu['COM'], mu['MES']

            else:
                validation, user_result = False, "The number you picked isn't optional"

        # Error has occurred, display error and try again.
        return self.display(user_result)

    @staticmethod
    def print_set(list_config):
        set_range = []

        for each in list_config:
            set_range.append(each['NMB'])

            # self.print_set the options available via self.config
            print('{}) {}'.format(each['NMB'], each['MES']))
        return set_range

    @staticmethod
    def header():
        print("{}".format("\nWelcome,\n"))

    #  return(boolean, int||str)
    @staticmethod
    def choice():
        x = input("Which option would you like? > ")
        try:
            return True, int(x)

        except:
            return False, "You chose '{}', which is a type={}.\nPlease pick again".format(x, type(x))
