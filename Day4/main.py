# Day 4 - Randomisation and Python Lists
# Day 4 - Project: Rock Paper Scissors - Game
import random

print("Welcome to Rock Paper Scissors")
players_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if players_hand == 0:
    print(rock)
elif players_hand == 1:
    print(paper)
elif players_hand == 2:
    print(scissors)

# Day4 examples and exercises
# number = random.randint(1, 10)
# print(number)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# coin_toss = random.randint(0, 1)
# if coin_toss == 1:
#     print("Heads")
# else:
#     print("Tails")

# states_of_america = ["Delaware", "Pennsylvania"]
# print(states_of_america)

# #Option 1
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# friends2 = ["Alice2", "Bob2", "Charlie2", "David2", "Emanuel2"]
# frin = [friends, friends2]
# print(frin[1][1])
# print(frin[1][4])
# list_length = len(friends)
# random_friend = random.randint(0, (list_length - 1))
# print(friends[random_friend])

# #Option 2
# print(random.choice(friends))