import errors
import re

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

def remove_blanks(wordToRemoveBlanksFrom):
    if "[" in wordToRemoveBlanksFrom or "]" in wordToRemoveBlanksFrom:
        blanklessWord = wordToRemoveBlanksFrom
        for blank in re.findall(r"\[\w\]", wordToRemoveBlanksFrom):
            blanklessWord = blanklessWord.replace(blank, "")
        return blanklessWord
    else:
        return wordToRemoveBlanksFrom

def verify_word(wordToVerify, wordList):
    startingLetter = wordToVerify[0]
    wordLength = str(len(wordToVerify))
    if wordToVerify not in wordList[startingLetter][wordLength]:
        return f"{wordToVerify.title()} is not a valid word in the Collins Scrabble dictionary!"
    else:
        return f"{wordToVerify.title()} is indeed a valid word in the Collins Scrabble dictionary!"

def word_value(word):
    if len(word) > 15:
        raise errors.WordTooLong(f"{word.title()} is {len(word) - 15} letters longer than the board!")
    total = 0
    word = remove_blanks(word)
    for letter in word:
        total += letter_value(letter)
    return total
