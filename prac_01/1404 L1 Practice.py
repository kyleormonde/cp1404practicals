NUMBER = 8

guess = int(input("1-10?"))
while guess != NUMBER:
    print("Incorrect")
    guess = int(input("1-10?"))
else:
    print("Correct")
