def main():
    MIN_LENGTH = 7
    password = get_valid_password(MIN_LENGTH)
    print_asterisks(password)


def get_valid_password(min_length):
    password = input(f"Enter the password: ")
    while len(password) < min_length:
        print(f"Password must meet at least {min_length} characters long.")
        password = input(f"Enter the password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
