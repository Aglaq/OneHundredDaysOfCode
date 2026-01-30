# Day 32 - Email SMTP and the datetime module
# Day 32 - Project: Automated Birthday Wisher
import datetime as dt
import pandas
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
new_birthday = input("Do you want to add new Birthday? Type 'y' for yes or 'n' for no.\n").lower()
if new_birthday == "y":
    new_name = input("Give name:\n")
    new_email = input("Give email address:\n")
    new_year = input("Give year:\n")
    new_month = input("Give month:\n")
    new_day = input("Give day:\n")
    birthdays.loc[len(birthdays)] = [new_name, new_email, new_year, new_month, new_day]

birthdays.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv

# Finding todays month and day
now = dt.datetime.now()
month_now = now.month
day_now = now.day

birthday_month = birthdays[birthdays.month == month_now]
birthday_day = birthday_month[birthday_month.day == day_now]
name = birthday_day.at[0, "name"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not birthday_day.empty:
    letter_number = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letter_number}.txt") as random_letter:
        letter = (random_letter.readlines())
        letter[0] = letter[0].replace("[NAME]", f"{name}")
    for line in letter:
        with open(f"./letter_templates/final_letter.txt", mode="a") as final_letter:
            final_letter.write(line)

# 4. Send the letter generated in step 3 to that person's email address.



# # Quote of the week
# import datetime as dt
# import smtplib
# import random

# my_email = ___
# password = ___

# # Finding day of the week
# now = dt.datetime.now()
# day_of_week = now.weekday()


# if day_of_week == 3:
#     # Opening txt file and changing to list
#     with open("quotes.txt") as quotes:
#         list_of_quotes = (quotes.readlines())

#     # Choosing random quote
#     random_quote = random.choice(list_of_quotes)

#     # Sending email
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, 
#                             to_addrs="___", 
#                             msg=f"Subject:Quote of the week!\n\n {random_quote}")

# import smtplib

# my_email = "testing101days@gmail.com"
# password = "bkmhzgrgfldcvybk"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="adamzubel@gmail.com", 
#                         msg="Subject:Hello\n\n This is body of the email!")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)

# date_of_birth = dt.datetime(year=1900, month=12, day=15)
# print(date_of_birth)
