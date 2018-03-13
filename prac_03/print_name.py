name = input("Name: ")
while not name:  # while name == ''
    print("Name cannot be blank.")
    name = str(input("Name: "))
#
for i in range(1, len(name), 2):
    print(name[i])


print(name[1::2])