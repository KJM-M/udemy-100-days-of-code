import requests
import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

today = datetime.date.today().strftime("%Y%m%d")


user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create user
# response = requests.post(pixela_endpoint, json=user_parameters)
# response.raise_for_status()

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/{GRAPH_ID}"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cyling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_data = {
    "date": today,
    "quantity": "555",
}

# post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(post_pixel_endpoint, json=pixel_data, headers=headers)

update_data = {
    "date": today,
}

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.put(update_endpoint, json=pixel_data, headers=headers)
# print(response.status_code)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(delete_endpoint, headers=headers)
print(response.status_code)
