from dotenv import load_dotenv
import json
import os
import requests

from pprint import pprint

load_dotenv()

apiKey = os.getenv("apiKey")
urlBase = "https://api.wordnik.com/v4/word.json/"

if __name__ == "__main__":
    scrabbleWord = input("Which word are you checking? ")
    scoreGet = requests.get(f"{urlBase}/{scrabbleWord}/scrabbleScore?api_key={apiKey}").text
    scoreGet = json.loads(scoreGet)
    pprint(scoreGet["value"])
