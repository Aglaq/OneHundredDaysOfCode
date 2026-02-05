# Day 33 - Application Programming Interfaces
# Day 33 - Project: ISS Overhead Notifier
import requests
from datetime import datetime
import smtplib

MY_LAT = 42.497681
MY_LNG = 27.470030
MY_EMAIL = "----"
PASSWORD = "----"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

def is_iss_close():
    return MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LNG-5 < iss_longitude < MY_LNG+5

def is_night():
    return sunset < time_now.hour or sunrise > time_now.hour

def is_iss_visible():
    return is_iss_close() and is_night()

# print(is_iss_close())
# print(is_night())
# print(is_iss_visible())
program_on = True

while program_on:
    if time_now.second == 0:       
        if is_iss_visible():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="----",
                                    msg="Subject:ISS Close!\n\nLook up!")




# Exercises Day 33
# import requests
# from datetime import datetime

# MY_LAT = 42.497681
# MY_LNG = 27.470030

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LNG,
#     "formatted": 0,
# }

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()

# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise)
# print(sunset)

# time_now = datetime.now()
# print(time_now.hour)

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
