import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo libro
url = f"{BASE_URL}/libros"
nuevo_libro = {"titulo": "The Lord of the rings", "autor": "Tolkien", "edicion": "2da edicion", "disponibilidad":"Media"}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Crear el segundo libro
libro_2 = {"titulo": "Game of thrones", "autor": "George R.R. Martin", "edicion": "3ra edicion", "disponibilidad":"Alta"}
response = requests.post(url, json=libro_2, headers=headers)
print("\nCreando el segundo libro:")
print(response.json())

# Obtener la lista de todos los libros
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de libros:")
print(response.json())

# Obtener un libro específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.get(url, headers=headers)
print("\nDetalles del libro con ID 1:")
print(response.json())

# Actualizar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/2"
datos_actualizacion = {"titulo": "Game of thrones", "autor": "George R.R. Martin", "edicion": "1ra edicion", "disponibilidad":"Baja"}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el libro con ID 2:")
print(response.json())

# Eliminar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el libro con ID 1:")
if response.status_code == 204:
    print(f"libro con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")