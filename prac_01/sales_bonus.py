"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
exit_condition = 0
while sales >= exit_condition:
    if sales < 1000:
        bonus = sales * 1.10 - sales
    else:
        bonus = sales * 1.15 - sales
    print("Bonus: $", "{:.2f}".format(bonus))
    # print("Total: $", "{:.2f}".format(sales + bonus))
    sales = float(input("Enter sales: $"))
pass
