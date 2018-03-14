def main():
    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def calculate_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32
