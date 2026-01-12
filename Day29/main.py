# Day 29 - Building a Password Manager GUI App with Tkinter
# Day 29 - Project: Password Manager
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

WHITE = "#FFFFFF"
BLACK = "#000000"
EMAIL = "2929az@az.pl"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = "WERT"
    email = "@email.com"
    password = "password123"
    with open("data.txt", "a") as d:
        d.write(f"\n{website} | {email} | {password}")

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
input_website = Entry(width=39, bg=WHITE, fg=BLACK, highlightthickness=0)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()
input_email = Entry(width=39, bg=WHITE, fg=BLACK, highlightthickness=0)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, EMAIL)
input_password = Entry(width=21, bg=WHITE, fg=BLACK, highlightthickness=0)
input_password.grid(column=1, row=3)

# Buttons
button_password = Button(text="Generate password", bg=WHITE, highlightbackground=WHITE)
button_password.grid(column=2, row=3)
button_password = Button(text="Add", width=37, bg=WHITE, highlightbackground=WHITE, command=save)
button_password.grid(column=1, row=4, columnspan=2)


window.mainloop()