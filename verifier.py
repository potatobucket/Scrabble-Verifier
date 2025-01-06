from dotenv import load_dotenv
import errors
import json
import os
import requests

load_dotenv()

apiKey = os.getenv("apiKey")
urlBase = "https://api.wordnik.com/v4/word.json/"

def get_scrabble_score(word):
    requestGet = requests.get(f"{urlBase}/{word}/scrabbleScore?api_key={apiKey}")
    if requestGet.status_code != 200:
        raise errors.WordNotFound(f"{word} is not a valid word in this dictionary!")
    else:
        scoreGet = json.loads(requestGet.text)
        return scoreGet["value"]

if __name__ == "__main__":
    scrabbleWord = get_scrabble_score(input("Which word are you checking? "))
    print(scrabbleWord)
