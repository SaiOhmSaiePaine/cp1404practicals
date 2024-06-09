"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
A ValueError occurs when a user enter the value of numerator or denominator that are not integer.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when a user try to enter denominator as 0 to divide numerator, so which cannot divide by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
As we handle ZeroDivisionError with EAFP: Easier to Ask Forgiveness than Permission, but we can avoid to change the code with LBYL: Look Before You Leap.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

