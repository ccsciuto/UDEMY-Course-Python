import requests
from datetime import datetime, date

USER = "cecesciuto"
TOKEN = "bjkdw7482bjf"
GRAPH_ID = "graph1"
# # created User
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": "bjkdw7482bjf",
    "username": "cecesciuto",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# creating a graph
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

update_graph1_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
today = date.today().strftime("%Y%m%d")
quantity = input("How many pages did you read today?")
graph1_config = {
    "date": today,
    "quantity": quantity,
}

update_response = requests.post(url=update_graph1_endpoint, json=graph1_config, headers=headers)
print(update_response.text)