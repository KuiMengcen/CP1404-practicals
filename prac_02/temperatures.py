MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """
        The main function of the driver.
        It will display a menu for the user to select Run the cycle until the user decides to exit by typing "Q".
    """
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """
        Convert Celsius to Fahrenheit.
    """
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
        Converts temperature from Fahrenheit to Celsius.
    """
    return 5/9 * (fahrenheit - 32)


main()