# Day 29 - Building a Password Manager GUI App with Tkinter
# Day 29 - Project: Password Manager
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #

WHITE = "#FFFFFF"
BLACK = "#000000"
EMAIL = "2929az@qsqsqs.pl"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }  
        }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="OOPS!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                input_website.delete(0, END)
                input_password.delete(0, END)
        else:
            # Updating old data with new one
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    website = input_website.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        try:
            data_web = data[website]
        except KeyError:
            messagebox.showerror(title="KeyError", message="No details for the website exists")
        else:
            messagebox.showinfo(title=website, message=f"Email: {data_web["email"]}\n"
                                                       f"Password: {data_web["password"]}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=WHITE, fg=BLACK)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3)

# Entries
input_website = Entry(width=22, bg=WHITE, fg=BLACK, highlightthickness=0)
input_website.grid(column=1, row=1)
input_website.focus()
input_email = Entry(width=39, bg=WHITE, fg=BLACK, highlightthickness=0)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, EMAIL)
input_password = Entry(width=22, bg=WHITE, fg=BLACK, highlightthickness=0)
input_password.grid(column=1, row=3)

# Buttons
button_password = Button(text="Generate password", width=12, bg=WHITE, highlightbackground=WHITE, command=generate_password)
button_password.grid(column=2, row=3)
button_add = Button(text="Add", width=37, bg=WHITE, highlightbackground=WHITE, command=save)
button_add.grid(column=1, row=4, columnspan=2)
button_search = Button(text="Search", width=12, bg=WHITE, highlightbackground=WHITE, command=find_password)
button_search.grid(column=2, row=1)

window.mainloop()