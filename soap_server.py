from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

#funcion de consulta
def saludar(nombre):
    return "!Hola, {}¡".format(nombre)

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

server = HTTPServer(("0.0.0.0",8000),SOAPHandler)
server.dispatcher = dispatcher
print("SErvidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()