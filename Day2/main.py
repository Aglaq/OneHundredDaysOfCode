# Day 2 - Understanding Data Types and How to Manipulate Strings
# Day 2 - Project: Tip Calculator

# Greeting
print("Welcome to the Tip Calculator!")
# Asking for bill in $ and for tip in % and number of payers
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15 ")
payers = input("How many people do split the bill? ")
# Calculating amount per person 
amount_to_pay = round(((float(bill) * (1 + int(tip) / 100)) / int(payers)), 2)
# Printing result
print(f"Each person should pay: ${amount_to_pay:.2f}")