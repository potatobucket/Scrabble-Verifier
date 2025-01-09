"""
A module to handle the logic for word verification and scoring.
"""

import errors
import json
import re

def add_multiplier(wordToMultiply: str):
    """
Adds a multiplier to either the letter or the entire word.

Each multiplier is denoted by a tag immediately preceding the letter:

    - $ : double letter
    - ^ : double word
    - & : triple letter
    - @ : triple word
    """
    doubleLetter: str = r"\$\w"
    doubleWord: str = r"\^\w"

    tripleLetter: str = r"\&\w"
    tripleWord: str = r"\@\w"

    doubleLetters: list = re.findall(doubleLetter, wordToMultiply)
    doubleWords: list = re.findall(doubleWord, wordToMultiply)
    tripleLetters: list = re.findall(tripleLetter, wordToMultiply)
    tripleWords: list = re.findall(tripleWord, wordToMultiply)

    for matchDoubleLetter in doubleLetters:
        doubledLetter: str = matchDoubleLetter[-1] * 2
        wordToMultiply = wordToMultiply.replace(matchDoubleLetter, doubledLetter)
    
    for matchTripleLetter in tripleLetters:
        tripledLetter: str = matchTripleLetter[-1] * 3
        wordToMultiply = wordToMultiply.replace(matchTripleLetter, tripledLetter)

    for matchedDoubleWord in doubleWords:
        doubleWordLetter: str = matchedDoubleWord[-1]
        wordToMultiply = wordToMultiply.replace(matchedDoubleWord, doubleWordLetter)
    wordToMultiply = wordToMultiply * 2 ** len(doubleWords)
    
    for matchedTripleWord in tripleWords:
        tripleWordLetter: str = matchedTripleWord[-1]
        wordToMultiply = wordToMultiply.replace(matchedTripleWord, tripleWordLetter)
    wordToMultiply = wordToMultiply * 3 ** len(tripleWords)

    return wordToMultiply

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
        blanklessWord: str = wordToRemoveBlanksFrom
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
    total: int = 0
    word = remove_blanks(word)
    word = add_multiplier(word)
    for letter in word:
        total += letter_value(letter)
    return total
