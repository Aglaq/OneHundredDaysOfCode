# Day 11 - Capstone Project
# Day 11 - The Black Jack
import art
import random

hit = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cpu_cards = []
player_cards = []


def random_card():
    return random.choice(cards)

def results():
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}")
    if sum(player_cards) > 21:
        print("You went over. You lose")
    elif sum(cpu_cards) > 21:
        print("Computer went over. You win")
    elif sum(cpu_cards) == sum(player_cards):
        print("Draw")
    elif sum(cpu_cards) > sum(player_cards):
        print("You lose")
    elif sum(cpu_cards) < sum(player_cards):
        print("You win!")

def black_jack():
    another_card = True
    print(art.logo)
    for i in range(2):
        cpu_cards.append(random_card())
        player_cards.append(random_card())
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {cpu_cards[0]}")
    while another_card:
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while hit not in ("y", "n"):
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == "y":
            player_cards.append(random_card())
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {cpu_cards[0]}")
        elif hit == "n":
            another_card = False
        if sum(player_cards) > 21:
            results()
            game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if game == "y":
                black_jack()
            elif game == "n":
                print("Bye bye!")
            else: 
                print("error")
        while sum(cpu_cards) < 17:
            cpu_cards.append(random_card())
        results()
        game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if game == "y":
            black_jack()
        elif game == "n":
            print("Bye bye!")
            return
        else: 
            print("error")
            return

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if game == "y":
    black_jack()
elif game == "n":
    print("Bye bye!")
else: 
    print("error")