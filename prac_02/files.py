# file_out = open("name_file.txt", 'w')
# user_name = input("Name? ")
# print(user_name, file=file_out)
# file_out.close()
#
# in_file = open('name_file.txt', 'r')
# get_user_name = in_file.read().title().strip('\n')
# print("Your name is {}.".format(get_user_name))
# in_file.close()

# numbers_file_in = open("numbers.txt", 'r')
# number1 = int(numbers_file_in.readline())
# number2 = int(numbers_file_in.readline())
# print(number1 + number2)
# numbers_file_in.close()

numbers_file_in = open("numbers.txt", 'r')
counter = 0
for line in numbers_file_in:
    number = int(line)
    counter += number
print(counter)
numbers_file_in.close()


