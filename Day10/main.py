# Day 10 - Functions with Outputs
# Day 10 - Project: The Calculator
import art

def add(n1, n2):
    return n1 + n2
    
def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

repetition = True
result = 0
power_on = True
basic_math = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


while power_on:
    repetition = True
    print(art.logo)
    first_number = float(input("What's the first number?: "))
    while repetition:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))

        result = basic_math[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        continuation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type any other letter to leave.\n")

        if continuation == 'y':
            first_number = result
        elif continuation == 'n':
            clear = print("\n" * 20)
            repetition = False
        else:
            power_on = False
            repetition = False

# Examples and exercises Day 10
# def is_leap_year(year):
#     """Checks if a year is leap by asking for input and returning boolean."""
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
    
# print(is_leap_year(int(input("Put a year: "))))

# def format_name(f_name, l_name): 
#     titled_f_name = f_name.title()
#     titled_l_name = l_name.title()
#     return titled_f_name + " " + titled_l_name
    
# formated_string = format_name("adam", "nowak")
# print(formated_string)