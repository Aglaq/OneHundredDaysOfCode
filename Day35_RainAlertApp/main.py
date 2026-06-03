# Day 35 - API Keys, Authentication, Environment Variables, and Sending SMS
# Day 35 - Rain Alert Application
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/foreast"
account_sid = "..."
auth_token = "..."

parameters = {
    "lat": 42.497681,
    "lon": 27.470030,
    "appid": "...",
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today! Remember to take an umbrella."
            from="..."
            to="..."
        )
    print(message.status)
