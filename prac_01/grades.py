"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if 90 <= score <= 100:
    print("Excellent")
elif score >= 50:
    print("Passable")
elif 0 <= score < 50:
    print("Bad")
else:
    print("Invalid score")
