# Day 5 - Python Loops
# Day 5 - Project: Password Generator



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

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)