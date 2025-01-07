#from dotenv import load_dotenv
#import errors
#import json
import letter_data as ld
#import os
#import requests

#load_dotenv()

#apiKey = os.getenv("apiKey")
#urlBase = "https://api.wordnik.com/v4/word.json/"

#def get_scrabble_score(word):
#    if len(word) > 15:
#        raise errors.WordTooLong("The maximum length of a word is 15 letters!")
#    requestGet = requests.get(f"{urlBase}/{word}/scrabbleScore?api_key={apiKey}")
#    if requestGet.status_code != 200:
#        raise errors.WordNotFound(f"{word} is not a valid word in this dictionary!")
#    else:
#        scoreGet = json.loads(requestGet.text)
#        return f"The Scrabble score for {word} is: {scoreGet["value"]}!"

if __name__ == "__main__":
    #scrabbleWord = get_scrabble_score(input("Which word are you checking? "))
    #print(scrabbleWord)

    scrabbleWord = ld.word_value(input("Which word are you checking? "))
    print(scrabbleWord)

    #print(ld.remove_blanks("quizzical"))
