menu_choice = str(input("\n1. Even numbers \n2. Odd numbers \n3. Squares \n4. Exit\n"))
# TODO: WHY do option 1, 2, and 3 print no \n though 4 does. Something to do with print(i, end'')?

while menu_choice != "4":

    if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
        first_number = int(input("First Number: "))
        second_number = int(input("Second Number: "))

    else:
        print("Invalid choice.")

    if menu_choice == "1":
        if first_number % 2 != 0:
            first_number = first_number + 1
        for i in range(first_number, second_number + 2, 2):
            print(i, end=" ")

    elif menu_choice == "2":
        if first_number % 2 != 1:
            first_number = first_number + 1
        for i in range(first_number, second_number + 2, 2):
            print(i, end=" ")

    elif menu_choice == "3":  # TODO: didn't use else because no. variable is undefined during menu choice != 1, 2, 3
        for i in range(first_number, second_number + 1, 1):
            print(i ** 2, end=" ")

    menu_choice = str(input("\n1. Even numbers \n2. Odd numbers \n3. Squares \n4. Exit\n"))

print("Finished")
