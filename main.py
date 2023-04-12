import random

NAME_FILE = "names.txt"


def get_names():

    names = []
    reader = get_read_and_file(NAME_FILE)

    while True:
        line = reader.readline().strip()

        if line == "":
            break

        names.append(line)

    return names


def get_read_and_file(name_file):
    return open(name_file)


def select_pairs_random(names):

    pairs = []

    name_one = ""
    name_two = ""

    while len(names) != 0:

        position_random = random.randint(0, len(names))
        name = names[position_random - 1]

        names.remove(name)

        if name_one == "":
            name_one = name
        else:
            name_two = name
            pairs.append(
                Pair(name_one, name_two)
            )

            name_one = ""
            name_two = ""

    return pairs


class Pair:

    def __init__(self, name_one, name_two):
        self.name_one = name_one
        self.name_two = name_two

    def get_name(self):
        return self.name_one

    def get_two(self):
        return self.name_two

    def get(self):
        return self.name_one + " , " + self.name_two


reader = get_read_and_file(NAME_FILE)
names = get_names()

pairs = select_pairs_random(names)

for pair in pairs:
    print(
        pair.get()
    )
