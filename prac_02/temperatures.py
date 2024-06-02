def main():
    show_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")

        else:
            print("Invalid option.")

        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 9.0 / 5
    return celsius


def show_menu():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)


main()
