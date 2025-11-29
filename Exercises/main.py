# Exercise 1: Calculate the multiplication and the sum od two numbers 

# number_one = float(input("What is first number?: "))
# number_two = float(input("What is second number?: "))
# multiply = print(f"Result of mulitply is: {number_one * number_two}.")
# add = print(f"Result of add is: {number_one + number_two}.")

# Exercise 2: Print the sum of a previous number and a current number

# sum = 0
# previous_number = 0

# for number in range(0, 10, 2):
#     sum = number + previous_number
#     print(f"Current number {number}, Previous number: {previous_number}, Sum: {sum}")

#     previous_number = number

# Exercise 3: Print characters present at an even index number

# original_string = input("Give me word: ")
# length = len(original_string)

# for number in range(0, length, 2):
#     print(original_string[number])

# Exercise 4: Remove first 'n' characters from a string

# def remove_chars(word, n):
#     new_word = ""

#     for number in range(0, len(word)):

#         if number > n - 1:
#             new_word += word[number]
    
#     print(new_word)

# original_word = input("Give any word: ")
# letter_cut = int(input("How many letters you want to cut?: "))
# remove_chars(original_word, letter_cut)

# Exercise 5: Check if the first and last numbers of a list are the same

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def list_check(list):
#     '''Checks if first and last number in list are the same'''
#     first_number = list[0]
#     last_number = list[len(list) - 1]
#     if first_number == last_number:
#         print(True)
#     else:
#         print(False)

# list_check(numbers_x)

# Exercise 6: Display numbers divisible by 5

# list = [10, 20, 33, 46, 55]

# for number in list:
#     modulo = number % 5

#     if modulo == 0:
#         print(number)

# Exercise 7: Find the number of occurrences of a substring in a string

# string = input("Give the sentence: ")
# word = input("What word are we counting? ")

# result = (string.count(word))
# print(f"{word} appeared {result} time(s).")

# Exercise 8: Print the following pattern

# for number in range(1, 6):
#     print(f"{number} " * number)

# Exercise 9: Check Palindrome Number

# original_number = input("Give number: ")
# number_listed = []
# true_or_false = []
# result = 0
# for number in original_number:

#     number_listed.append(number)

# for index in range(0, len(original_number)):

#     if number_listed[index] == number_listed[len(original_number) - index - 1]:
#         result += 1

# if result == len(original_number):
#     print(f"Yes. {original_number} is a palindrome")
# else:
#     print(f"No. {original_number} isn't a palindrome")

# Exercise 10: Merge two lists using the following codition. New list must contain all odd numbers from list one and even from list two.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# result_list = []

# for number in list1:
#     modulo = number % 2
#     if modulo != 0:
#         result_list.append(number)

# for number in list2:
#     modulo = number % 2
#     if modulo == 0:
#         result_list.append(number)

# print(result_list)

# Exercise 11: Get each digit from a number in the reverse order.

