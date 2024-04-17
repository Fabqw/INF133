import requests

url = 'http://localhost:5000/'
response = requests.get(url)

if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)
    
params = {'nombre': 'Fabricio'}
response = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print(mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    

response = requests.get(url+'/sumar?num1=5&num2=3')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print(mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    
response = requests.get(url+'/palindromo?cadena="reconocer"')
if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print(mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)
    
response = requests.get(url + '/contar?cadena=”exepciones”&vocal=”e”')

if response.status_code == 200:
    data = response.json()
    cantidad = data['cantidad']
    print(f"La cantidad de vocales es: {cantidad}")
else:
    # Si hay un error, imprimimos el código de estado de la respuesta
    print("Error al conectar con el servidor (GET):", response.status_code)
    
