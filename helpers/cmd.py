import os


def clear():
    c = os.system('cls' if os.name == 'nt' else 'clear')
    return c