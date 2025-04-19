from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from word_class import Word

app = FastAPI()

origins: list = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

wordQuery: Word

@app.get("/")
async def hello_world():
    return "Hello, world!"

@app.get("/check-word")
async def check_word(word: str):
    """
Checks a word for score, validity and definition.
    """
    wordQuery = Word(word = word)
    return wordQuery.results
