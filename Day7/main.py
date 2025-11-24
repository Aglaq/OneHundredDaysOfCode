# Day 7 - Hangman
# Day 7 - Project: Hangman

# importing modules
import random
import art_hangman
import words_lists

# variables
game_over = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
placeholder = ""

# LOGO
print(art_hangman.logo)

# randomisation
chosen_word = random.choice(words_lists.words)
for n in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()
    # print(guess)
    
    for n, letter in enumerate(chosen_word):
        if letter == guess:
            # print("Right")
            display += letter
        elif letter == placeholder[n]:
            display += placeholder[n]
            # print(display)
        else:
            # print("Wrong")
            display += "_"
    print(display)
    if placeholder == display:
        lives -= 1
        print(lives)
    placeholder = display
    print(art_hangman.hangman_stages[lives])
    if lives == 0:
        game_over = True
        print("You lost!")
    # print(placeholder)
    if "_" not in placeholder:
        game_over = True
        print("You won!")