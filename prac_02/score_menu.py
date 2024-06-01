def main():
    small_num = 0
    high_num = 100
    score = get_valid_score(small_num, high_num)

    show_menu()
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "P":
            check_score(score)
        elif choice == "S":
            show_asterisks(score)
        else:
            print("Invalid option.")

        choice = input("Enter choice: ").upper()
    print("farewell.")


def show_menu():
    menu = """(P)rint result
(S)how stars 
(Q)uit """
    print(menu)


def get_valid_score(small_num, high_num):
    score = int(input("Enter your score: "))
    while score > high_num or score < small_num:
        print("Invalid score.")
        score = int(input("Enter your score: "))
    return score


def show_asterisks(score):
    print('*' * score)


def check_score(score):
    if score < 0:
        print(f"Invalid score.")
    else:
        if score > 100:
            print("Invalid score.")
        elif score >= 90:
            print(f"{score} is Excellent.")
        elif score >= 50:
            print(f"{score} is Passable.")
        else:
            print(f"{score} is Bad.")


main()
