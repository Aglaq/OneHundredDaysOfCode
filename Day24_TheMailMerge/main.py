# Day 24 - Files, Directories and Paths
# Day 24 - Project: the Mail Merge

with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    list_of_names = (names_file.readlines())
    list_of_names = [name.strip() for name in list_of_names]
for name in list_of_names:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter = (letter_file.readlines())
        letter[0] = letter[0].replace("[name]", f"{name}")
        for line in letter:
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a") as completed_letter:
                completed_letter.write(line)

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Examples for day 24, High Score was added to Snake Game in day 20
# with open("my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file:
#     file.write("New text")
