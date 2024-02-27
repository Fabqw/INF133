from zeep import Client

client = Client(
    "http://localhost:8000/"
)

# peticion o requests
result = client.service.Saludar("Fabricio")
result2 = client.service.Sumar(1,2)
print(result)
print(result2)
