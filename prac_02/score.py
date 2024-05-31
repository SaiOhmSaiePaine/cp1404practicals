def main():
    score = float(input("Enter score: "))
    check_score(score)


def check_score(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif score > 50:
            print("Passable")
        elif score > 90:
            print("Excellent")
        else:
            print("Bad")


main()
