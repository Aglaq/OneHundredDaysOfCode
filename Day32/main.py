# Day 32 - Email SMTP and the datetime module
# Day 32 - Project: Automated Birthday Wisher





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
