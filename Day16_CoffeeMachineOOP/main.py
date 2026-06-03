# Day 16 - Object Oriented Programming (OOP)
# Day 16 - Project: Coffee Machine in OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drink = Menu()

machine_on = True
while machine_on:
    options = drink.get_items()
    program = input(f"What would you like? ({options}): ")
    while program not in ("espresso", "latte", "cappuccino", "report", "off"):
        program = input(f"What would you like? ({options}): ")
    if program == "off":
        print("Bye bye!")
        machine_on = False
    elif program == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = drink.find_drink(program)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)














# Examples and Exercises Day 16
# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("SpringGreen")
# timmy.forward(100)

# turtle.done()

# my_screen = Screen()
# print(my_screen.canvheight)

# from prettytable import PrettyTable

# table = PrettyTable()
# table.field_names = ["Day", "Exercise"]
# table.add_row([16, "Start Day 16 project"])
# table.add_row([17, "Example for Day 17"])

# print(table)

# try:
#     from prettytable import PrettyTable
#     print("PrettyTable is working!")
# except Exception as e:
#     print("NOT working:", e)

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

