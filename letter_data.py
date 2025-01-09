"""
A module to handle the logic for word verification and scoring.
"""

import errors
import json
import re

def add_multiplier(wordToMultiply: str):
    """
Adds a multiplier to either the letter or the entire word.
    """
    pass

def define_word(wordToDefine: str):
    """
Returns the definition of a given word.
    """
    return "THERE ARE NO DEFINITIONS IN SCRABBLE! ONLY WORDS!"

def letter_value(letter: str):
    """
Assigns a number value to a letter based on its frequency in English words.
    """
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
    elif letter == "_":
        return 0

def remove_blanks(wordToRemoveBlanksFrom: str):
    """
Removes the blank tiles from a word using a tag system (i.e. if a letter is inside squarenthesis ([z]) it gets removed from the word).
    """
    if "[" in wordToRemoveBlanksFrom or "]" in wordToRemoveBlanksFrom:
        blanklessWord = wordToRemoveBlanksFrom
        for blank in re.findall(r"\[\w\]", wordToRemoveBlanksFrom):
            blanklessWord = blanklessWord.replace(blank, "_")
        return blanklessWord
    else:
        return wordToRemoveBlanksFrom

def valid_length(wordToMeasure: str):
    """
Checks if a word is a legal length for a Scrabble play.
    """
    if len(wordToMeasure) < 2:
        raise errors.WordTooShort(f"{wordToMeasure.title()} is shorter than any legal move! Not valid!")
    elif len(wordToMeasure) > 15:
        raise errors.WordTooLong(f"{wordToMeasure.title()} is {len(wordToMeasure) - 15} letters longer than the board! Not valid!")
    else:
        return True

def verify_word(wordToVerify: str):
    """
Verifies whether or not a word is a valid word in the Collins Scrabble dictionary.
    """
    if valid_length(wordToVerify):
        with open("words_json.json") as words:
            wordList: dict = json.load(words)
        startingLetter: str = wordToVerify[0]
        wordLength: str = str(len(wordToVerify))
        if wordToVerify not in wordList[startingLetter][wordLength]:
            return f"{wordToVerify.title()} is not a valid word in the Collins Scrabble dictionary!"
        else:
            return f"{wordToVerify.title()} is indeed a valid word in the Collins Scrabble dictionary!"

def word_value(word: str):
    """
Tallies up the value of a given word.
    """
    if valid_length(word):
        total: int = 0
        word: str = remove_blanks(word)
        for letter in word:
            total += letter_value(letter)
        return total
