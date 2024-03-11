import requests
        # 
        # estudiantePorId(id:1){
        #     nombre
        #     apellido
        #     carrera
        # }
# Definir la consulta GraphQL
query_lista ="""
    {
        estudiantes{
            id
            nombre   
            carrera         
        }
    }
"""
query = """
    {
        estudiantesCarrera(carrera:"Arquitectura"){
            id
            nombre
        }
    }
"""
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }    
"""
query_actualizar = """
mutation{
    actualizarEstudiante(id:2){
        carera
    }
}
"""

# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

response2 = requests.post(url, json={'query':query_crear})
print(response2.text)

response3 = requests.post(url, json={'query': query_lista})
print(response3.text)

response4 = requests.post(url, json={'query': query_eliminar})
print(response4.text)

response5 = requests.post(url, json={'query': query_actualizar})
print(response5.text)

response3 = requests.post(url, json={'query': query_lista})
print(response3.text)