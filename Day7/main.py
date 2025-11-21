# Day 7 - Hangman
# Day 7 - Project: Hangman

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for n in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
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
    placeholder = display
    # print(placeholder)
    if "_" not in placeholder:
        game_over = True
        print("You won!")