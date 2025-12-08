# Day 15 - Coffee Machine
# Day 15 - Project: Coffee Machine

import menu

# Starting resources
starting_water = 300
starting_milk = 200
starting_coffee = 10
starting_money = 0
machine_on = True

water_amount = starting_water
milk_amount = starting_milk
coffee_amount = starting_coffee
money_amount = starting_money

def check_resources(coffee_type):
    water_left = water_amount - menu.MENU[coffee_type]["ingredients"]["water"]
    if water_left < 0:
        print("Sorry, there is not enough water.")
        return 0
    milk_left = milk_amount - menu.MENU[coffee_type]["ingredients"]["milk"]
    if milk_left < 0:
        print("Sorry, there is not enough milk.")
        return 0
    coffee_left = coffee_amount - menu.MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_left < 0:
        print("Sorry, there is not enough coffee.")
        return 0
    print(water_left, milk_left, coffee_left)

def coins(price):
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))
    coins_sum = (quarters_amount * 25 + dimes_amount * 10 + nickles_amount * 5 + pennies_amount * 1) / 100
    print(coins_sum)
    rest = float("{:.2f}".format(coins_sum - price))
    return rest


def coffee_machine(type):
    '''Prepares choosen coffee and returns updated resources values.'''
    out_of_resources = check_resources(type)
    if out_of_resources == 0:
        return
    change = coins(3)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        print(f"Here is ${change} in change.")
        print(f"Here is your {type}. Enjoy!")
        return

while machine_on:
    function = input("What would you like? (espresso/latte/cappuccino): ")
    while function not in ("espresso", "latte", "cappuccino", "report", "off"):
        function = input("What would you like? (espresso/latte/cappuccino): ")
    if function == "espresso" or function == "latte" or function == "cappuccino":
        coffee_machine(function)
    elif function == "report":
        print(f"Water: {water_amount}ml")
        print(f"Milk: {milk_amount}ml")
        print(f"Coffee: {coffee_amount}g")
        print(f"Money: ${money_amount}")
    elif function == "off":
        machine_on = False
