from zeep import Client

client = Client(
    "http://localhost:8000/"
)

# peticion o requests
result = client.service.Saludar("Fabricio")
print(result)