#  HTTP requests : GET, POST, PUT, DELETE
# GET: Get the data from the server
# POST: Send data to the server. example posting data to google sheets or posting a tweet on Twitter using the APIs
# PUT: Update the data on the server
# DELETE: Delete the data on the server
import requests
from datetime import datetime

USER_NAME = "nithin"
TOKEN = "token"
pixela_endpoint = "https://pixe"
GRAPH_ID = "graph1"

parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# step 1 : creating a user account:
# response = requests.post(url=pixela_endpoint, json=parameters)  # the parameter is in json format
# print(response.text)  # text property gives the response as a text. can be used to check if there's any issues in data

# step 2: creating a graph definition:

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu"
}

# creating header in request for security so that secret or sensitive content doesn't appear on typing
# authenticating ourselves with a header
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# step 3 : post a value to the graph:

add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

# using datetime and strftime method to enter date automatically.
# strftime method is used to format the date the way we want it to be.

# today = datetime(year=2022,month=7,day=15) to add pixels for a particular date
# print(today.strftime("%Y%m%d"))

today = datetime.now()

add_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you learn? "),
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_config, headers=headers)
print(response.text)

# updating data using put request:
pixel_update_config = {
    "quantity": "7.5"
}
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

#  delete a particular post
# pixel_deletion_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# print(response.text)
