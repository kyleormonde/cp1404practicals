"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!

def main():
    score = float(input("Enter score: "))
    result = find_result(score)
    print(result)


def find_result(score):
    if score < 0 or score > 100:
        result = "Invalid Score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
