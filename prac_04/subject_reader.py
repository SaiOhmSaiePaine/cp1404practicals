"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_detail(data)


def load_data():
    input_file = open(FILENAME)
    with open(FILENAME, 'r') as input_file:
        subjects = []
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            subjects.append(parts)
    return subjects


def display_subject_detail(data):
    for information in data:
        print(f"{information[0]} is taught by {information[1]} and has {str(information[2])} students. ")


main()



