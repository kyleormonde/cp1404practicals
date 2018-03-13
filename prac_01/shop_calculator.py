number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of Items!")
    number_of_items = int(input("Number of Items: "))

total_price = 0
for i in range(number_of_items):
    # item_list.append(float(input("Price of Item: ")))
    price = (float(input("Price of item: ")))
    total_price = price + total_price

if total_price > 100:
    total_price = total_price * .9

print("Total price for", number_of_items, "items is ${:.2f}".format(total_price))
