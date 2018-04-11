numbers = []

index = 1
number = int(input("Number {}: ".format(index)))
while number >= 0:
        numbers.append(number)
        index += 1
        number = int(input("Number {}:".format(index)))
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))
