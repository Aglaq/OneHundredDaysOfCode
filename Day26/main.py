# Day 26 - List Comprehension
# Day 26 - Project: NATO Alphabet
import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}


while True:
    user_word = input("Enter a word: ").upper()
    try:
        user_word_final = [nato_alphabet_dict[code] for code in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(user_word_final)
        break


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
