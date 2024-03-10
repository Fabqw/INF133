import requests

# consulta Graphql

query = """
    {
        estudiante(id:1, nombre:"jose"){
            nombre
        }
    }
"""
# server graphql
url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query':query})
print(response.text)