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
    return random_word.upper()

#Display word progress to user.
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

#Get user to input their guesses.
def get_user_guess():
    """Prompt user to enter a guess by entering a letter.

    Returns:
        user_guess: (string) - the users guess.
    """
    prompt = True
    while prompt:
        user_guess = input("Please guess a letter. ").upper()
        if user_guess.isalpha() == False:
            print("Invalid input. Please enter a letter.")
        elif user_guess == "":
            print("Invalid input. Please enter a letter.")
        else:
           prompt = False
           return user_guess
           
#Create dictionary to track game progress and stats.
def game_state():
    """Track game progress using a dictionary.

    return game_dict: (dict) - the dictionary housing the game data.
    """
    #Initialize the dictionary.
    game_dict = {
        "Correct Guesses": [],
        "Incorrect Guesses": [],
        "Remaining attempts": 6
        }
    return game_dict