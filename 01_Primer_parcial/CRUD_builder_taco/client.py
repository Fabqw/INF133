import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}
print("-- POST ---")
mi_taco = {
    "base": "Grande",
    "guiso": "Carne",
    "toppings": ["Jamon", "Queso"],
    "salsa": "Verde"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())
print("-- GET ---")
response = requests.get(url)
print(response.json())
print("-- PUT---")
edit_taco = {
    "salsa": "Roja"
}
new_url = url+"/1"
response = requests.put(new_url, json=edit_taco)
print(response.json())

response = requests.get(url)
print(response.json())

print("-- DELETE ---")
response = requests.delete(url + "/1")
print(response.json())

response = requests.get(url)
print(response.json())