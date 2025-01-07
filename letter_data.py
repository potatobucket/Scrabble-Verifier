def letter_value(letter):
    letter = letter.lower()
    if letter in "aeilnorstu":
        return 1
    elif letter in "dg":
        return 2
    elif letter in "bcmp":
        return 3
    elif letter in "fhvwy":
        return 4
    elif letter == "k":
        return 5
    elif letter in "jx":
        return 8
    elif letter in "zq":
        return 10

def word_value(word):
    total = 0
    for letter in word:
        total += letter_value(letter)
    return total
