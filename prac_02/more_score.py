import random


def main():

    score_number = int(input("Enter the number of scores: "))
    random_scores = []

    for i in range(score_number):
        random_score = random.randint(0, 100)
        check_score(random_score)
        random_scores.append(random_score)

    print(random_scores)
    write_to_file(random_scores, "results.txt")


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


def write_to_file(scores, file):
    with open(file, "w") as file:
        for score in scores:
            file.writelines(str(score) + "\n")


main()

