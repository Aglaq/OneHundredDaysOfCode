# Day 7 - Hangman
# Day 7 - Project: Hangman

# importing modules
import random
import art_hangman
import words_lists

# variables
game_over = False
lives = 6
placeholder = ""
incorrect_letters = []

# LOGO
print(art_hangman.logo)

# randomisation and placeholder made of "_"
chosen_word = random.choice(words_lists.words)
for n in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# main while loop - core game
while not game_over:

    display = ""
    guess = input("Guess a letter: ").lower()
    
    # if letter was correct
    for n, letter in enumerate(chosen_word):
        if letter == guess:
            display += letter
        elif letter == placeholder[n]:
            display += placeholder[n]
        else:
            display += "_"

    # checking if life was lost
    if guess not in chosen_word and guess not in incorrect_letters:
        lives -= 1
        incorrect_letters.append(guess)
        print(f"There is no letter '{guess}'. You lose a life!")
    elif guess not in chosen_word and guess in incorrect_letters:
        print(f"You've already guessed letter '{guess}'")
    else:
        print(f"There is a letter '{guess}'")

    print(display)
    print(f"****************************** {lives}/6 LIVES LEFT ******************************")
    print(art_hangman.hangman_stages[lives])

    placeholder = display

    if lives == 0:
        game_over = True
        print("******************** YOU LOSE *******************")
        print(f"The word was: '{chosen_word}'")

    if "_" not in placeholder:
        game_over = True
        print("******************** YOU WIN *******************")