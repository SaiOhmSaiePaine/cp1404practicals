"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

"""
show MENU
get choice 
while choice != Q
    if choice == C
        get celsius 
        fahrenheit = celsius * 9.0 / 5 + 32
        show fahrenheit
    else if choice == F
        get fahrenheit 
        celsius = (fahrenheit - 32) * 9.0 / 5
        show celsius
    else
        show Invalid option
    show MENU
    get choice 
print Thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) * 9.0 / 5
        print(f"Result: {celsius:.2f} C")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
