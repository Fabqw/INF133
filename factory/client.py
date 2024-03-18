import requests
url = "http://localhost:8000/delivery"
headers = {"Content-Type": "application/json"}

vehicle_type = "motorcycle"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
print(response.text)

vehicle_type = "drone"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
print(response.text)

vehicle_type = "scout"
data = {"vehicle_type": vehicle_type}
response = requests.post(url, json=data, headers=headers)
print(response.text)