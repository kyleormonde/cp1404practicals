def main():
    name = get_name()
    steps = int(input("How many steps between letters: "))
    print_name(name, steps)


def get_name():
    name = input("Name: ")
    # while name.strip(' ') == ''
    while not name:
        print("Name cannot be blank.")
        name = str(input("Name: "))
    return name


def print_name(name, steps):
    for i in range(0, len(name), steps):
        print(name[i])
        # print(name[1::2])


main()
