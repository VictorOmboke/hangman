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

#Display word progress to user
def display_word(word_to_guess):
    """Display the word as underscores and update when user guesses correct.

    Parameters:
        word_to_guess: (string) - the randomly chosen word that the user is trying to guess.    

    Returns:
        word_display: (string) - the word to be guessed.
    """
    #Display the word to be guessed as underscores.
    word_display = "_ " * len(word_to_guess)
    return word_display

#Create dictionary to track game progress and stats
def game_state():
    """Track game progress using a dictionary.

    return game_dict: (dict) - the dictionary housing the game data.
    """
    #Initialize the dictionary
    game_dict = {
        "Correct Guesses": [],
        "Incorrect Guesses": [],
        "Remaining attempts": 6
        }