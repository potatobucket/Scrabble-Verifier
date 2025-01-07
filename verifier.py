import letter_data as ld

if __name__ == "__main__":
    #scrabbleWord = get_scrabble_score(input("Which word are you checking? "))
    #print(scrabbleWord)

    scrabbleWord = ld.word_value(input("Which word are you checking? "))
    print(scrabbleWord)

    #print(ld.remove_blanks("quizzical"))
