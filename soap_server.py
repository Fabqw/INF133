from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

#funcion de consulta
def saludar(nombre):
    return "!Hola, {}¡".format(nombre)

def sumar(num1, num2):
    resultado = num1 + num2
    return "La suma de {} y {} es: {}".format(num1, num2, resultado)

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

#El que va adespachar el resultado del endpoit
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace = True,
    ns = True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "Sumar",
    sumar,
    returns={"resultado": str},
    args={"num1": int, "num2": int},
)

dispatcher.register_function(
    "EsPalindromo",
    es_palindromo,
    returns={"esPalindromo": bool},
    args={"palabra": str},
)


server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()