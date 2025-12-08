# Day 14 - Higher or Lower
# Day 14 - Project: Higher or Lower Game
import random
import art
import game_data

# print(art.logo)
# print(game_data.data)

def random_item():
    '''Choooses random person from game_data.'''
    return random.choice(game_data.data)

def comparison(list_one, list_two):
    '''Compares which person has more followers and returns result.'''
    followers_A = item_A["follower_count"]
    followers_B = item_B["follower_count"]
    # print(followers_A)
    # print(followers_B)
    bigger = 0
    if followers_A > followers_B:
        bigger = "A"
    else:
        bigger = "B"
    return bigger

game = True
points = 0
item_A = random_item()
item_B = random_item()
if item_A == item_B:
    item_B = random_item()

print("\n" * 20)
print(art.logo)
while game == True:
    print(f"Compare A: {item_A["name"]}, a {item_A["profession"]}, from {item_A["country"]}.")
    print("")
    print(art.vs)
    print("")
    print(f"Against B: {item_B["name"]}, a {item_B["profession"]}, from {item_B["country"]}.")
    players_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    while players_choice not in ("A", "B"):
        players_choice = input("Not recognized symbol. Type 'A' or 'B': ").capitalize()
    print("\n" * 20)
    print(art.logo)

    result = comparison(item_A, item_B)
    if players_choice == result:
        points += 1
        item_A = item_B
        item_B = random_item()
        print(f"You're right! Current score: {points}.")
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        game = False