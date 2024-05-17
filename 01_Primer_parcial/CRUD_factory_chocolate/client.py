import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

print("-- Post --")

new_chocolate = {
    "chocolate_type": "tableta",
    "peso": 10,
    "sabor": "fresa"    
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

new_chocolate = {
    "chocolate_type": "bombon",
    "peso": 15,
    "sabor": "nuez",
    "relleno": "fresa"
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

new_chocolate = {
    "chocolate_type": "trufa",
    "peso": 20,
    "sabor": "oreo",
    "relleno": "vainila"    
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

print("-- Get --")

response = requests.get(url=url)
print(response.json())

print("--- Put ---")

chocolate_id_to_update = 1
updated_chocolate = {
    "sabor": "vainilla"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate)
print("Chocolate actualizado:", response.json())

response = requests.get(url=url)
print(response.json())

print("--- Delete ---")
chocolate_id_to_delete = 2
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

response = requests.get(url=url)
print(response.json())

new_chocolate = {
    "chocolate_type": "trufa",
    "peso": 20,
    "sabor": "oreo",
    "relleno": "mango"    
}
response = requests.post(url=url, json=new_chocolate, headers=headers)
print(response.json())

response = requests.get(url=url)
print(response.json())
