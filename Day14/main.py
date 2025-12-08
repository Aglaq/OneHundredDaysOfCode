# Day 14 - Higher or Lower
# Day 14 - Project: Higher or Lower Game
import random
import art
import game_data

# print(art.logo)
# print(game_data.data)

def random_item():
    '''Function that chooses random list from game_data.'''
    return random.choice(game_data.data)

def comparison(list_one, list_two):
    '''Function that compares which person has more followers and returns result.'''
    followers_A = item_A["follower_count"]
    followers_B = item_B["follower_count"]
    # print(followers_A)
    # print(followers_B)
    bigger = 0
    if followers_A > followers_B:
        bigger = "A"
    elif followers_A < followers_B:
        bigger = "B"
    return bigger

game = True
points = 0
item_A = random_item()
item_B = random_item()

print("\n" * 20)
print(art.logo)
while game == True:
    print(f"Compare A: {item_A["name"]}, {item_A["profession"]}, from {item_A["country"]}.")
    print("")
    print(art.vs)
    print("")
    print(f"Against B: {item_B["name"]}, {item_B["profession"]}, from {item_B["country"]}.")
    players_choice = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    # print(players_choice)

    result = comparison(item_A, item_B)
    if players_choice == result:
        points += 1
        item_A = item_B
        item_B = random_item()
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {points}.")
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {points}")
        game = False