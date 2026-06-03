# Day 15 - Coffee Machine
# Day 15 - Project: Coffee Machine

import menu

# Starting resources
starting_water = 3000
starting_milk = 2000
starting_coffee = 1000
starting_money = 0
machine_on = True

water_amount = starting_water
milk_amount = starting_milk
coffee_amount = starting_coffee
money_amount = starting_money

def check_resource(amount, cost, product):
    left = amount - cost
    if left < 0:
        print(f"Sorry there is not enough {product}.")
        return -1
    
def coins(price):
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters?: "))
    dimes_amount = int(input("How many dimes?: "))
    nickles_amount = int(input("How many nickles?: "))
    pennies_amount = int(input("How many pennies?: "))
    coins_sum = (quarters_amount * 25 + dimes_amount * 10 + nickles_amount * 5 + pennies_amount * 1) / 100
    # print(coins_sum)
    rest = float("{:.2f}".format(coins_sum - price))
    return rest

def coffee_machine(w_amount, m_amount, c_amount, coffee_type):
    '''Prepares choosen coffee and returns updated resources values.'''
    water = check_resource(w_amount, menu.MENU[coffee_type]["ingredients"]["water"], "water")
    if water == -1:
        return 0, 0, 0, 0
    milk = check_resource(m_amount, menu.MENU[coffee_type]["ingredients"]["milk"], "milk")
    if milk == -1:
        return 0, 0, 0, 0
    coffee = check_resource(c_amount, menu.MENU[coffee_type]["ingredients"]["coffee"], "coffee")
    if coffee == -1:
        return 0, 0, 0, 0
    change = coins(menu.MENU[coffee_type]["cost"])
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return 0, 0, 0, 0
    else:
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type}. Enjoy!")
        minus_water = menu.MENU[coffee_type]["ingredients"]["water"]
        minus_milk = menu.MENU[coffee_type]["ingredients"]["milk"]
        minus_coffee = menu.MENU[coffee_type]["ingredients"]["coffee"]
        plus_money = menu.MENU[coffee_type]["cost"]
        return minus_water, minus_milk, minus_coffee, plus_money

def report():
    '''Gives report about actual status of resources.'''
    print(f"Water: {water_amount}ml")
    print(f"Milk: {milk_amount}ml")
    print(f"Coffee: {coffee_amount}g")
    print(f"Money: ${money_amount}")

while machine_on:
    program = input("What would you like? (espresso/latte/cappuccino): ")
    while program not in ("espresso", "latte", "cappuccino", "report", "off"):
        program = input("What would you like? (espresso/latte/cappuccino): ")
    if program == "espresso" or program == "latte" or program == "cappuccino":
        sum_water, sum_milk, sum_coffee, sum_money = coffee_machine(water_amount, milk_amount, coffee_amount, program)
        water_amount -= sum_water
        milk_amount -= sum_milk
        coffee_amount -= sum_coffee
        money_amount += sum_money
    elif program == "report":
        report()
    elif program == "off":
        machine_on = False
