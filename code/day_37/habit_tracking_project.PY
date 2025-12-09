import requests
from datetime import datetime


USERNAME = "dwarakesh"
TOKEN = "vbskbkfsbfvkfbksf"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response =  requests.post(url=pixela_endpoint, json=user_parameters)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today?: ")
}

# response =  requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_data = {
    "quantity": "0.45"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
