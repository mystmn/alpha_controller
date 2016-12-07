class TestEnv(object):
    instanceVar = 2

    def __init__(self, var):
        self.class_name = __name__
        self.var = var
        self.dictionary = {
            'a': "Name",
            'b': "Age",
        }

    @classmethod
    def calling(x):
        return "What class am I = {}\n".format(x.__name__)

    def prev_calling(self):
        return "{}".format(self.class_name)

    @classmethod
    def unknown(*args):
        print("{}".format(args))

    @staticmethod
    def colors():
        return calling(), TestEnv.calling()

    def added_number(self, x):
        return x + "Bobby's World"

    def __getattr__(self, x):

        try:
            if self.dictionary[x] == "Name":
                return self.var + " " + self.added_number(x)

            elif self.dictionary[x] == "Age":
                return self.var + " " + "Pacman"

            else:
                return self.unknown(x)
        except:
            return "Not found"


def calling(*args):
    print("And go {}!".format(args))


def a():
    return


TE = TestEnv("")
print(TestEnv("TestB").b)  # __getattr__

print("1) {}".format(TE.a))  # __getattr__
print("2) {}".format(TE.b))  # __getattr__

'''
TestEnv.unknown("Settings Are good")
inv = TestEnv.instanceVar

print(TE.calling())
print(TE.prev_calling())
print(TestEnv.unknown([inv]))
print(TestEnv.colors())
'''