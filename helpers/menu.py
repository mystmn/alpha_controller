from helpers import cmd

# NMB = menu selector
# MES = Message of display
# COM = command to be executed
menu_options = [
    {
        'NMB': 0,
        'MES': "scan for models",
        'COM': [
            "jpg",
            "html",
            "doc",
            "bimp",
        ]
    },
    {
        'NMB': 1,
        'MES': "ultimate",
        'COM': [
            "jpg",
            "html",
            "doc",
            "bimp",
            "png",
        ]
    },
    {
        'NMB': 2,
        'MES': "run setup",
        'COM': "Firing the engines"
    }
]


#  return menu[int(NMB), str(MSG), str(COM)]
def display(error=()):

    if error is not ():
        cmd.clear()
        print("p={}\n".format(error))

    else:
        # Display a one time HEADER
        header()

    menu_range = print_menu(menu_options)

    validation, user_result = choice()

    if validation:
        #  Is the user_result even optional
        if user_result in menu_range:
            mu = menu_options[user_result]
            return mu['NMB'], mu['COM'], mu['MES']

        else:
            validation, user_result = False, "The number you picked isn't optional"

    #  Error has occurred, display error and try again.
    return display(user_result)


def print_menu(x):
    set_range = []

    for each in x:
        set_range.append(each['NMB'])

        # Print the options available via menu_options
        print('{}) {}'.format(each['NMB'], each['MES']))
    return set_range


def header():
    print("{}".format("\nWelcome, go ahead and pick\n"))


#  return(boolean, int||str)
def choice():
    x = input("Which option would you like? > ")
    try:
        return True, int(x)

    except:
        return False, "You chose '{}', which is a type={}.\nPlease pick again".format(x, type(x))