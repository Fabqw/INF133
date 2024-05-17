import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

pizza = {
    "tamaño": 10,
    "masa": "delgada",
    "toppings": ["jamon", "queso"]
}

response = requests.post(url, json=pizza, headers=headers)
print(response.json())