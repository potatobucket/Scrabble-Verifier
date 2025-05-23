import letter_data as ld
from pydantic import BaseModel

class Word(BaseModel):
    """
A word.
    """
    word: str
    
    @property
    def definition(self):
        """
    The definition of the word as it pertains to the game.
        """
        return ld.define_word(self.word)

    @property
    def base_letter_scores(self):
        """
    The scores for each individual tile.
        """
        return {f"{letter}": ld.letter_value(letter) for letter in self.word}

    @property
    def value(self):
        """
    The value of the word. Includes letter- and word-multipliers.
        """
        return ld.word_value(self.word)
    
    @property
    def verification(self):
        """
    Is this a valid word for the game?
        """
        return ld.verify_word(self.word)
    
    @property
    def results(self):
        """
    Returns all the key | value pairs you could ever want!
        """
        return {
            "word": self.word,
            "value": self.value,
            "tileScores": self.base_letter_scores,
            "valid": self.verification,
            "definition": self.definition
        }
