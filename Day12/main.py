# Day 12 - Scope
# Day 12 - Project: Number Guessing Game
import random
import art

difficulty = "0"

def game(lives):

    number_to_guess = random.randint(1, 100)
    # print(number_to_guess)

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess < number_to_guess:
            print("Too low.")
            print("Guess again")
            lives -= 1
        elif user_guess > number_to_guess:
            print("Too high.")
            print("Guess again")
            lives -= 1
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return

    print("You've run out of guesses. GAME OVER")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
while difficulty not in ("easy", "hard"):
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    game(10)
elif difficulty == "hard":
    game(5)





# Examples and exercises Day 12

# def is_prime(num):
#     '''Checks if provided number is prime.'''
#     nums = [2, 3, 5, 7]
#     if num in nums:
#         return True
#     elif num % 2 == 0:
#         return False
#     elif num % 3 == 0:
#         return False
#     elif num % 5 == 0:
#         return False
#     elif num % 7 == 0:
#         return False
#     else:
#         return True

# print(is_prime(123))
