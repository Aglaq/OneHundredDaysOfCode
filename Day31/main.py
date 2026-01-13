# Day 31 - Capstone Project
# Day 31 - Project: Flash Card App
from tkinter import *
import pandas
import random
#----------------------------CONSTANTS-------------------------------

BACKGROUND_COLOR = "#B1DDC6"
LANG_1 = "French"
LANG_2 = "English"

#----------------------RANDOM_CARD--------------------------

# Reading CSV file with pandas
words_list_data = pandas.read_csv("data/french_words.csv")
# Changing DataFrame to list of dictionaries
words_list = [{f: e} for f, e in zip(words_list_data[LANG_1], words_list_data[LANG_2])]

def choosing_random_card():
    random_card = random.choice(words_list)
    random_word = (list(random_card.keys())[0])
    canvas.itemconfig(language_text, text=LANG_1)
    canvas.itemconfig(word_text, text=random_word)

#-------------------------------GUI----------------------------------

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=choosing_random_card)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR, command=choosing_random_card)
wrong_button.grid(column=0, row=1)

choosing_random_card()

window.mainloop()