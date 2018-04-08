import random

# TODO: Ask user for number of quick picks.
# TODO: Generate that many lines of 6 random numbers
# TODO: Between 1-45. Store values as constant.
# TODO: Numbers in line must be unique.
# TODO: Sort line by ascending order

MAX_RAND = 45
MIN_RAND = 1
SIZE_OF_QP = 6

times = int(input("How many quick picks: "))
for i in range(times):
    quick_pick = []
    for k in range(SIZE_OF_QP):
        number = random.randint(MIN_RAND, MAX_RAND)
        while number in quick_pick:
            number = random.randint(MIN_RAND, MAX_RAND)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))
    # for number in quick_pick:
    #     print(" ".join("{:2}".format(number)))
