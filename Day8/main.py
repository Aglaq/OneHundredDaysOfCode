# Day 8 - Functions with Inputs
# Day 8 - Project: Caesar Cipher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted = ""
    for letter in original_text:
        index = alphabet.index(letter)
        new_index = index + shift_amount
        if new_index > 25:
            new_index = new_index - 26
        encrypted += alphabet[new_index]
        # print(index)
    print(encrypted)

encrypt(text, shift)

# Exercises and examples day 8
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("All good!")

# greet()

# Function with 1 input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print("All good!")

# greet_with_name("Adam")

# Function with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name} from {location}!")

# greet_with("Adam", "Krakow")
# greet_with(location = "Krakow", name = "Adam")

# def calculate_love_score(name1, name2):
#     name1_lower = name1.lower() 
#     name2_lower = name2.lower()
#     string = name1_lower + name2_lower
#     true = "true"
#     love = "love"
#     sum1 = 0
#     sum2 = 0
#     for letter in true:
#         sum1 += string.count(letter)
    
#     for letter in love:
#         sum2 += string.count(letter)
        
#     string_sum1 = str(sum1) 
#     string_sum2 = str(sum2)

#     final = string_sum1 + string_sum2
#     print(final)
    
# calculate_love_score("Kanye West", "Kim Kardashian")
