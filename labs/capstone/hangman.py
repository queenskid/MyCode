#!/usr/bin/env python3

import random

def main():
    # start of game message
    welcome = ['Welcome to Hangman! Guess the secret word letter by letter.',
               'If you win, you will get to continue to the next game']
    # loop to print the message complete
    for line in welcome:
        print(line, sep='\n')

    # This will keep the loop true thoughout until condition is not met.

    play_again = True

    while play_again:

        # word bank for game.
        words = ["clock", "python", "computer", "camera", "sneakers",
                 "football", "giants", "murder", "hannibal", "dexter"]
        # randomizing and setting to lowercase a word from the bank to a variable.
        chosen_word = random.choice(words).lower()
        # setting this variable to null, to keep track of the guesses attempts by the user.
        player_guess = None
        # emtpy array to pass in guessed letters from the user
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            # create a blank version of the secret word selected at random. this will help in drawing out the dashes for the user to track attempt.
            word_guessed.append("-")
        # joins the words in the list word_guessed
        joined_word = None

        Display = (
"""
-----
|   |
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|
--------
"""
)

        print(Display[0])
        attempts = len(Display) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nSelect a letter between A-Z" + "\n> ")).lower()
            except:
                print("NOT a valid input. Please try again.")
                continue
            else:
                # check to make sure user input is a letter.
                if not player_guess.isalpha():
                    print("NOT a letter DUMMY. Please try again.")
                    continue
                # check the input is only one letter.
                elif len(player_guess) > 1:
                    print("Only one latter at a time. Please try again.")
                    continue
                # check to see if the letter was already used.
                elif player_guess in guessed_letters:
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    # replace all letters in the chosen word that match the user's guess.
                    word_guessed[letter] = player_guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(Display[(len(Display) - 1) - attempts])
        # This check to see if there are any dashes left in the word being guessed.
        if "-" not in word_guessed:
            print(("\nCongratulations, you won! You guessed {}, to win the game").format(chosen_word))
        # if none are left and word was not guessed, game loop will end.
        else:
            print(("\nYou suck at this! The word was {}.").format(chosen_word))

        print("\nWould you like to play again? enter yes or y to play again. Enter any key to QUIT.")

        response = input("Entry: ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
