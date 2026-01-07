# Day 27 - Tkinter, *args, **kwargs and GUI Programs
# Day 27 - Project: Miles to Kilometers converter
from tkinter import *

# 1 mile = 1.609 km
def convert():
    kilometres = float(input_miles.get()) * 1.609
    result.config(text=f"{kilometres}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=120)
window.config(padx=20, pady=20)

# Labels

# Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Kilometres
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Equal
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Result
result = Label(text="")
result.grid(column=1, row=1)

# Entries

# User input
input_miles = Entry(width=7)
input_miles.grid(column=1, row=0)

# Buttons

# Calculate
calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()