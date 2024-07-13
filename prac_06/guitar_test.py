"""
languages
Estimate: 15 minutes
Actual: 16 minutes
"""

from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
another_guitar = Guitar('Another Guitar', 2013, 1550)

print(f"{guitar.name} get_age() - Expect {100}. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expect {9}. Got {another_guitar.get_age()}")
print()

print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")
print()

print(guitar)
print(another_guitar)
