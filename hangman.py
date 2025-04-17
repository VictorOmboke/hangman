#Import list of words from words.py.
from words import words_list
#Import random module.
import random

def game_state():
    """Track game progress using a dictionary.

    return game_dict: (dict) - the dictionary housing the game data.
    """
    #Initialize the dictionary.
    game_dict = {
        "Incorrect Guesses": [],
        "Remaining Attempts": 6,
        "Current Display": "",
        "Game Over": False
        }
    return game_dict

def word_selector():
    """Select a random word from the list of words.

    Returns:
        random_word: (string) - a random word from the words list.
    """
    #Randomly select and store any word from the words list.
    random_word = random.choice(words_list)
    #Return the random word in uppercase letters.
    return random_word.upper()

def word_display(word_to_guess):
    """Display the word as underscores and update when user guesses correct.

    Args:
        word_to_guess: (string) - the randomly chosen word that the user is trying to guess.    

    Returns:
        word_display: (string) - the word to be guessed.
    """
    #Display the word to be guessed as underscores.
    word_display = "_" * len(word_to_guess)
    return word_display

def update_word_display(word_to_guess, user_guess, word_display):
    """Update the word display when the user guesses the word correctly.

    Args:
        word_to_guess (str): the word to be guessed.
        user_guess (str): the users guess.
        word_display (str): current display of guessed/un-guessed letters.

    Returns:
        updated_word_display: (str) - an updated version of the word display.
    """
    #store the index of each occurrence of the users guess in the word to be guessed.
    occurrences = [i for i, letter in enumerate(word_to_guess) if letter == user_guess]
    #Convert word to guess into list.
    word_display_list = list(word_display)
    #Replace underscores with correctly guessed letters.
    for i in occurrences:
        word_display_list[i] = user_guess
    #Turn the list back to into a string
    updated_word_display = ''.join(word_display_list)
    return updated_word_display

def get_user_guess():
    """Prompt user to enter a guess by entering a letter.
    Returns:
        user_guess: (string) - the users guess.
    """
    prompt = True
    while prompt:
        user_guess = input("Please guess a letter. ").upper()
        #Handle if the users guess is not an alphabetical letter.
        if user_guess.isalpha() == False:
            print("Invalid input. Please enter a letter.")
        #Handle if the user enters nothing.
        elif user_guess == "":
            print("Invalid input. Please enter a letter.")
        #End the loop and return the users acceptable input.
        else:
           prompt = False
           return user_guess
        
def process_guess(user_guess, word_to_guess, game_state):
    """Determine if the player's guess is correct or not and handle word display and update game state.

    Args:
        player_guess (str): the players guess.
        word_to_guess (str): the word to be guessed.
        game_state (dict): A dictionary tracking the games stats.
    """
    #Handle if the player made the correct guess.
    if user_guess in word_to_guess:
        #Update the display in the game_state dictionary.
        game_state["Current Display"] = update_word_display(word_to_guess, user_guess, game_state["Current Display"])
        #Display the updated word to be guessed.
        print(game_state["Current Display"])
        print("You made a correct guess!")
        #Display incorrect guesses.
        print(f"Your incorrect guesses: {game_state["Incorrect Guesses"]}")
        #Display remaining attempts.
        print(f"Your remaining attempts: {game_state["Remaining Attempts"]}")
    #Handle when the user makes the same incorrect guess twice.
    elif user_guess in game_state["Incorrect Guesses"]:
        print("You have already guessed that letter. Try again!")
    #Handle when the player made an incorrect guess.
    else:
        #Add the users incorrect guesses to the dictionary.
        game_state["Incorrect Guesses"].append(user_guess)
        #Remove one of their attempts.
        game_state["Remaining Attempts"] -= 1
        print("Incorrect guess, try again!")
        #Display the users incorrect guesses.
        print(f"Your incorrect guesses: {", ".join(game_state["Incorrect Guesses"])}")
        #Display the users remaining attempts.
        print(f"Your remaining attempts: {game_state["Remaining Attempts"]}")

def play_again():
    """Prompt user to play again.
    """
    #Initialize acceptable answers in a list.
    answer = ["yes", "no"]
    prompt = True
    while prompt:
        user_input = input("Would you like to play the game again? (Enter 'yes' or 'no') ").lower()
        #Check if the users input is an acceptable answer and play the game again.
        if user_input == "yes":
            prompt = False
            print("Great, have fun!")
            play_game()
        #Check if the users input is an acceptable answer and end the game.
        elif user_input == "no":
            prompt = False
            print("Thank you for playing!")
        #Handle any other input.
        elif user_input not in answer:
            print("Invalid input. Please enter 'yes' or 'no'.")

def results(game_state, word_to_guess):
    """Determine if the user has won or lost the game.

    Args:
        game_state (dict): holds the current stats of the game.
        word_to_guess (str): the word to be guessed
    """
    #Handle when the user runs out of attempts.
    if game_state["Remaining Attempts"] == 0:
        #Update the 'Game Over' key in the dictionary.
        game_state["Game Over"] = True
        print("Game over!")
        print("You are all out of attempts.")
        print(f"The correct word was: {word_to_guess}")
        #Ask user to play again.
        play_again()
    #Handle if the user guesses the word correctly.
    elif "_" not in game_state["Current Display"]:
        game_state["Game Over"] = True
        print("You Win!")
        print(f"You correctly guessed the word {word_to_guess}!")
        play_again()

def play_game():
    """Play the game by using a loop.
    """
    game = game_state()
    word_to_guess = word_selector()
    #Store the current word display
    game["Current Display"] = word_display(word_to_guess)
    print(f"Guess the word: {game["Current Display"]}")
    #Initialize while loop to play multiple rounds of the game.
    while game["Remaining Attempts"] > 0 and not game["Game Over"]: 
        user_guess = get_user_guess()
        #Provide feedback for each guess.
        process_guess(user_guess, word_to_guess, game)
        #Display the results of the game.
        results(game, word_to_guess)
#play the game
play_game()