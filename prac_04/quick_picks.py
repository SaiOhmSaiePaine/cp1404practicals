import random

"""
How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
"""

MINIMUM = 1
MAXIMUM = 45
NUMBER_PER_LINE = 6

quick_pick_number = int(input("How many quick picks? "))
while quick_pick_number <= 0:
    print("The quick pick number can not be less than 0.")
    quick_pick_number = int(input("How many quick picks? "))

for row in range(quick_pick_number):
    quick_pick_numbers = []
    for column in range(NUMBER_PER_LINE):
        random_number = random.randint(MINIMUM, MAXIMUM)
        while random_number in quick_pick_numbers:
            random_number = random.randint(MINIMUM, MAXIMUM)
        quick_pick_numbers.append(random_number)
    quick_pick_numbers.sort()

    print(" ".join(f"{number:2}" for number in quick_pick_numbers))



