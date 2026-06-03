# Day 38 - Exercise Tracking with Python and Google Sheets
# Day 38 - Exercise Tracking
import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 182
AGE = 35
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER_TOKEN = os.environ.get("TOKEN")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise = input("Tell me which exercises you did: ")

params = {
    "query": exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nut_response = requests.post(url=nutrition_endpoint, json=params, headers=headers)
duration = nut_response.json()["exercises"][0]["duration_min"]
calories = nut_response.json()["exercises"][0]["nf_calories"]
activity_name = (nut_response.json()["exercises"][0]["name"]).title()

sheety_endpoint = os.environ.get("SHEET_ENDPOINT")

headers_sheety = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

today = datetime.today().strftime("%d/%m/%Y")
time = datetime.today().strftime("%X")

exercise_data = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": activity_name,
        "duration": duration,
        "calories": calories,
    }
}

response = requests.post(url=sheety_endpoint, json=exercise_data, headers=headers_sheety)
