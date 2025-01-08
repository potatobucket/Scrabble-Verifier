# Scrabble Verifier
The program is now capable of checking the following:
 
  - **word validity**:
    - whether a word is too short or too long to be a valid move in the game
    - whether or not a word is listed in the dictionary
	    - the dictionary is sorted into a JSON file that splits words first by alphabet and then by length

  - **word scoring**:
    - each letter is assigned a value individually
    - blanks are marked with a set of squarenthesis around the letter (e.g. [w]) and are automatically stripped from the word using regular expressions as blanks are worth zero points
    - after the blanks are stripped the value of each remaining letter is added together

  - **offline access**:
    - by using a JSON file instead of an API call the program is now 100% independent and requires no online connection.
	    - the API--while useful--proved inadequate for my needs and this new data structure is both more robust and more complete as it uses the same list of words as one of the official Scrabble dictionaries used in tournament play.