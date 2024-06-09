# First program
name = input("Enter name: ")
out_file = open("name.txt", "w")

print(name, file=out_file)

# Second Program
in_file = open("name.txt", "r")

print(f"Hello Mr.{in_file.read().strip()}!!")
# print(in_file.readline().strip())
# print(in_file.readlines())
# for line in in_file:
#     print(line)
out_file.close()
in_file.close()

# Third Program
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)


# Fourth Program
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
