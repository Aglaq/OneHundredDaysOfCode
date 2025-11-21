# Day 7 - Hangman
# Day 7 - Project: Hangman

import random
import art_hangman

game_over = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
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