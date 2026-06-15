
# 📘 Assignment: Hangman — Word Guessing Game

## 🎯 Objective

Build a command-line Hangman game that reinforces string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Implement the Hangman game

#### Description
Write a Python CLI program that:

- Chooses a secret word at random from a predefined list (or file).
- Prompts the player to guess single letters (case-insensitive) until the word is revealed or attempts are exhausted.
- Shows current word progress using underscores for unknown letters and reveals correct guesses.
- Tracks letters guessed and the remaining incorrect attempts.
- Ends with a clear win or lose message.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list or text file.
- Accept single-letter guesses and ignore repeated guesses.
- Display the current progress in the format: `_ a _ _ m a n`.
- Decrease remaining attempts when the guessed letter is not in the word.
- Finish and print a win message with the correct word when guessed.
- Finish and print a loss message showing the correct word when attempts reach zero.
- Provide a `starter-code.py` file with a `main()` entry point in this folder.

#### Example gameplay
```
Word: _ _ _ _ _ _
Guess a letter: p
Word: p _ _ _ _ _
Guess a letter: z
Incorrect. Attempts left: 5
...
You win! The word was "python".
```

