# Day 37 - Advanced Authentication and POST / PUT / DELETE Requests
# Day 37 - Project: Habit Tracking
import requests
from datetime import datetime

USERNAME = "..."
TOKEN = "..."
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Step 1 - Create your user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step 2 - Create a graph definition

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
    }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Step 4 Post Value to the Graph

posting_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.today().strftime('%Y%m%d')
today_distance = str(8.5)

posting_data = {
    "date": today,
    "quantity": today_distance,
}

# response = requests.post(url=posting_endpoint, json=posting_data, headers=headers)
# print(response.text)

