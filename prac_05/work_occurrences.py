"""
Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""

text = input("Text: ")
characters = text.split()
print(characters)
dict_characters = {}
for character in characters:
    dict_characters[character] = characters.count(character)

max_length = max((len(word) for word in dict_characters))
for character, count_number in sorted(dict_characters.items()):
    print(f"{character:{max_length}} = {count_number}")
