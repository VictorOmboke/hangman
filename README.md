# Hangman Game

A classic word-guessing game built with Python, where players guess letters to uncover a hidden word before running out of attempts.

## Features

✔️ **Random word selection** from a predefined list.  
✔️ **Live game state tracking**: Incorrect guesses, remaining attempts, and current progress.  
✔️ **Case-insensitive input**: Accepts both lowercase/uppercase letters.  
✔️ **Win/lose detection**: Stops automatically when the word is guessed or attempts run out.  
✔️ **Play again option**: Restarts the game without rerunning the script.

## How to Run

1. **Prerequisites**:

   - Python 3.x installed.

2. **Steps**:

   - Clone/download the project files.
   - Navigate to the project directory in your terminal.
   - Run:
     ```bash
     python hangman.py
     ```

3. **Gameplay**:
   - Guess letters one at a time.
   - Correct guesses reveal letters in the word.
   - Incorrect guesses reduce remaining attempts.
   - Win by guessing all letters before attempts run out!

## Project Structure

- `hangman.py`: Main game logic.
- `words.py`: List of words for the game (customizable).

## Customization

- **Add your own words**: Edit `words.py` to include new words or categories.
- **Adjust difficulty**: Change `Remaining Attempts` in the `game_state()` function.
