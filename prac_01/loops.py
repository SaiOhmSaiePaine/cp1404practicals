for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
for j in range(0, 110, 10):
    print(j, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
for k in range(20, 0, -1):
    print(k, end=' ')
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
number_star = int(input("Number of stars: "))
print("*" * number_star)
print()

# d. print n lines of increasing stars. Print lines of increasing stars,
# starting at 1 with no blank line.

for n in range(number_star + 1):
    print(n * "*")

