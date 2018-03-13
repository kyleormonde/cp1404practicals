user_name = str(input("Enter name: "))
menu_choice = str(input("(H)ello \n(G)oodbye \n(Q)uit \n"))

while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello", user_name + ".")
    elif menu_choice == "G":
        print("Goodbye", user_name + ".")
    else:
        print("Invalid choice.")

    menu_choice = str(input("(H)ello \n(G)oodbye \n(Q)uit \n"))

print("Finished")
