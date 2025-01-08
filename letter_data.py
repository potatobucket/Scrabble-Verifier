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

def valid_length(wordToMeasure):
    if len(wordToMeasure) < 2:
        raise errors.WordTooShort(f"{wordToMeasure.title()} is shorter than any legal move! Not valid!")
    elif len(wordToMeasure) > 15:
        raise errors.WordTooLong(f"{wordToMeasure.title()} is {len(wordToMeasure) - 15} letters longer than the board! Not valid!")
    else:
        return True

def verify_word(wordToVerify, wordList):
    if valid_length(wordToVerify):
        startingLetter = wordToVerify[0]
        wordLength = str(len(wordToVerify))
        if wordToVerify not in wordList[startingLetter][wordLength]:
            return f"{wordToVerify.title()} is not a valid word in the Collins Scrabble dictionary!"
        else:
            return f"{wordToVerify.title()} is indeed a valid word in the Collins Scrabble dictionary!"

def word_value(word):
    if valid_length(word):
        total = 0
        word = remove_blanks(word)
        for letter in word:
            total += letter_value(letter)
        return total
