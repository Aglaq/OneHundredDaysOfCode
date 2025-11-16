# Day 5 - Python Loops
# Day 5 - Project: Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

for letter in range(nr_letters):
    random_letter = random.randint(0, (len(letters) - 1))
    password.append(letters[random_letter])
for number in range(nr_numbers):
    random_number = random.randint(0, (len(numbers) - 1))
    password.append(numbers[random_number])
for letter in range(nr_symbols):
    random_symbol = random.randint(0, (len(symbols) - 1))
    password.append(symbols[random_symbol])

password_str = "".join(password) 
print(f"Your password is: {password_str}")

mixed_password = random.sample(password, len(password))
mixed_password_str = "".join(mixed_password)
print(f"Your password is: {mixed_password_str}")

# Day 5 exercises and examples
# print("Hello, Day 5!")
# student_scores = [150, 142, 185, 120,171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]
# print(max(student_scores))
# maximum = 0
# for student in student_scores:
#     if student > maximum:
#         maximum = student
# print(maximum)

# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)

# for number in range(1, 101):
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)