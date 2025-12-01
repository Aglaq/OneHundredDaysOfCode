# Day 11 - Capstone Project
# Day 11 - The Black Jack
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cpu_cards = []
player_cards = []

def random_card():
    rdm_card = random.choice(cards)
    return rdm_card

def black_jack():
    
    print(art.logo)
    for i in range(2):
        rdm_card = 0
        random_card()
        print(rdm_card)
        cpu_cards.append(rdm_card)
        random_card()
        player_cards.append(rdm_card)
    print(cpu_cards)
    print(player_cards)

rdm_card = 0
random_card()
print(rdm_card)
cpu_cards.append(rdm_card)
print(cpu_cards)
game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if game == "y":
    black_jack()
elif game == "n":
    print("Bye bye!")
else: 
    print("error")