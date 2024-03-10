import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"

### Inciso a

# # GET para mostrar todas las carreras
ruta_get_carreras = url + "/carreras/"
get_response_carreras = requests.request(method="GET", url=ruta_get_carreras)
print(get_response_carreras.text)

### Inciso b

# # GET para mostrar a los estudiantes de la carrera de "Economia"
ruta_get_eco = url + "/economia/"
get_response_eco = requests.request(method="GET", url=ruta_get_eco)
print(get_response_eco.text)

### Inciso C 

# # POST agrega un nuevo estudiante por la ruta /economia

ruta_post_eco = url + "economia/"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
}
post_response_eco = requests.request(method="POST", url=ruta_post_eco, json=nuevo_estudiante)
#print(post_response_eco.text)

# segundo estudiante
ruta_post_eco = url + "economia/"
nuevo_estudiante = {
    "nombre": "Raquel",
    "apellido": "Suarez",
}
post_response_eco = requests.request(method="POST", url=ruta_post_eco, json=nuevo_estudiante)
#print(post_response_eco.text)

# # GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# # DELETE elimina todos los estudiantes por la ruta /estudiantes
# ruta_eliminar = url + "estudiantes"
# eliminar_response = requests.request(method="DELETE", 
#                                     url=ruta_eliminar)
# print(eliminar_response.text)

# # PUT actualiza un estudiante por la ruta /estudiantes
# ruta_actualizar = url + "estudiantes"
# estudiante_actualizado = {
#     "id": 1,
#     "nombre": "Juan",
#     "apellido": "Pérez",
#     "carrera": "Ingeniería Agronomica",
# }
# put_response = requests.request(
#     method="PUT", url=ruta_actualizar, 
#     json=estudiante_actualizado
# )
# print(put_response.text)