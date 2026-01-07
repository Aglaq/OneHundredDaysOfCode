def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)
result = add(5, 6, 7, 8)
print(result)

from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Button 2

my_button = Button(text="New Button", command=button_clicked)
my_button.grid(row=0, column=2)

# Entry

input = Entry(width=10)
input.grid(row=2, column=3)
# user_message = input.get()


window.mainloop()