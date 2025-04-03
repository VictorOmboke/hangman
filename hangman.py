#Import list of words from words.py.
from words import words_list
#Import random module.
import random

#Randomly select a word from the words list.
def word_selector():
    """Select a random word from the list of words.

    Returns:
        random_word: (string) - a random word from the words list.
    """
    #Randomly select and store any word from the words list.
    random_word = random.choice(words_list)
    return random_word

#Create dictionary to track game progress and stats
def game_state():
    """Track game progress using a dictionary.

    return game_dict: (dict) - the dictionary housing the game data.
    """
    #Initialize the dictionary
    game_dict = {
        "Correct Guesses": [],
        "Incorrect Guesses": [],
        "Remaining attempts": 6,
        "Word display": ""
        }