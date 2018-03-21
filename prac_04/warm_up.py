numbers = [3, 1, 4, 1, 5, 9, 2]

# 3, 2, 1, list - 2], 1, true, false, false, list + new list

# print(numbers[0])
# print(numbers[-1])
# print(numbers[3])
# print(numbers[:-1])
# print(numbers[3:4])
# console...

numbers[0] = 10
print(numbers)
numbers[len(numbers) - 1] = 1
print(numbers)
get_all = numbers[2:len(numbers)]
print(get_all)
if 9 in numbers:
    print(True)
else:
    print(False)