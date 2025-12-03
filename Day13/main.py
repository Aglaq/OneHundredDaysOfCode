# Day 13 - Debugging
# Day 13 - Project
import random

# print("Hello, Day 13!")

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = new_item + item
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 4, 7, 12, 13])