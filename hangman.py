#Import list of words from words.py.
from words import words_list
#Import random module.
import random

#Create dictionary to track game progress and stats.
def game_state():
    """Track game progress using a dictionary.

    return game_dict: (dict) - the dictionary housing the game data.
    """
    #Initialize the dictionary.
    game_dict = {
        "Incorrect Guesses": [],
        "Remaining Attempts": 6
        }
    return game_dict

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
def word_display(word_to_guess):
    """Display the word as underscores and update when user guesses correct.

    Parameters:
        word_to_guess: (string) - the randomly chosen word that the user is trying to guess.    

    Returns:
        word_display: (string) - the word to be guessed.
    """
    #Display the word to be guessed as underscores.
    word_display = "_" * len(word_to_guess)
    return word_display

#Update the word display when the user guesses a word correctly.
def update_word_display(word_to_guess, user_guess, word_display):
    """Update the word display when the user guesses the word correctly.

    Args:
        word_to_guess (str): the word to be guessed.
        user_guess (str): the users guess.
        word_display (str): current display of guessed/un-guessed letters.

    Returns:
        str: an updated version of the word display.
    """
    #store the index of each occurrence of the users guess in the word to e guessed.
    occurrences = [i for i, letter in enumerate(word_to_guess) if letter == user_guess]
    #Convert word to guess into list.
    word_display_list = list(word_display)
    #Replace spaces with correctly guessed letters.
    for i in occurrences:
        word_display_list[i] = user_guess
    #Turn the list back to into a string
    updated_word_display = ' '.join(word_display_list)
    return updated_word_display

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
        
#Process the  players guess
def process_guess(user_guess, word_to_guess, game_state, word_display):
    """Determine if the player's guess is correct or not and handle word display and update game state.

    Args:
        player_guess (str): the players guess.
        word_to_guess (str): the word to be guessed.
        game_state (dict): A dictionary tracking the games stats.
        word_display: (str): current display of guessed/un-guessed letters.

    Returns:
        _type_: _description_
    """
    #Handle if the player made the correct guess.
    if user_guess in word_to_guess:
        print(update_word_display(word_to_guess, user_guess, word_display))
        print("You made a correct guess!")
        print(f"Your incorrect guesses: {game_state["Incorrect Guesses"]}")
        print(f"Your remaining attempts: {game_state["Remaining Attempts"]}")
    #Handle when the player made an incorrect guess.
    else:
        game_state["Incorrect Guesses"].append(user_guess)
        game_state["Remaining Attempts"] -= 1
        print("Incorrect guess, try again!")
        print(f"Your incorrect guesses: {", ".join(game_state["Incorrect Guesses"])}")
        print(f"Your remaining attempts: {game_state["Remaining Attempts"]}")

#word = word_selector()
#print(f"Word to guess: {word}")
#game = game_state()
#guess = get_user_guess()
#display = word_display(word)
#print(f"Word display: {display}")
#process_guess(guess, word, game, display)

#Ask user if they would like to play again.
def play_again():
    """Prompt user to play again.
    """
    answer = ["yes", "no"]
    prompt = True
    while prompt:
        user_input = input("Would you like to play the game again? (Enter 'yes' or 'no') ").lower()
        if user_input in answer and user_input == "yes":
            prompt = False
            print("Great, have fun!")
            #call function to play the game
        elif user_input in answer and user_input == "no":
            prompt = False
            print("Thank you for playing!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

print(play_again())

#Determine if the user has won or lost.
def results(game_state, word_to_guess):
    """Determine if the user has won or lost the game.

    Args:
        game_state (dict): holds the current stats of the game.
    """
    if game_state["Remaining Attempts"] == 0:
        print("Game over!")
        print("You are all out of attempts.")
        print(f"The correct word was: {word_to_guess}")
        #Prompt the user to enter yes or no if they wish to play the game again or not.
    #determine how to declare the user a winner, loop over the display word to see if there are any remaining '_' and if there are none, they win!