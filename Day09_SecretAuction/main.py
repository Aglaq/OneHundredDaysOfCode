# Day 9 - Dictionaries and Nesting
# Day 9 - Project: Secret Auction

import logo

repetition = True
bidders = {}

print(logo.logo)
print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_dictionary):
    highest_bidder = 0

    for amount in bidders.values():
        if amount > highest_bidder:
            highest_bidder = amount 
    for bidder in bidders:
        if highest_bidder == bidders[bidder]:
            print(f"The winner is {bidder} with a bid of ${bidders[bidder]}.\n")

while repetition:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n$"))
    # print(type(bid))
    bidders[name] = bid  
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear = print("\n" * 20)

    if more_bidders == "no":
        repetition = False
        find_highest_bidder(bidders)


        


# Examples and exercises Day 9
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student in student_scores:
#     if 90 < student_scores[student]:
#         student_grades[student] = "Outstanding"
#     elif 80 < student_scores[student]:
#         student_grades[student] = "Exceeds Expectations"
#     elif 70 < student_scores[student]:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)


# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]   
# }
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# }
# print(travel_log["Germany"]["cities_visited"][2])