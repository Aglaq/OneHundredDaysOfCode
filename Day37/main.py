# Day 37 - Advanced Authentication and POST / PUT / DELETE Requests
# Day 37 - Project: Habit Tracking
import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "xkfivy368snchfr2",
    "username": "Aglaq",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

requests.post(url=pixela_endpoint, json=)