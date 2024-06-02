def main():
    SMALL_NUM = 0
    HIGH_NUM = 100
    score = get_valid_score(SMALL_NUM, HIGH_NUM)

    show_menu()
    choice = input("Enter choice: ").upper()

    while choice != "Q":
        if choice == "P":
            result = check_score(score)
            print(f"{score} is {result}. ")
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
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"


main()
