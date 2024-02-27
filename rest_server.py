from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Fabricio",
        "apellido": "Quispe",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Pedro",
        "apellido": "Lima",
        "carrera": "Ingeniería de software",
    },
    {
        "id": 3,
        "nombre": "Pepe",
        "apellido": "Lima",
        "carrera": "Ingeniería de desarrollo",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == '/buscar_nombre':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            nombres_con_P = [estudiante['nombre'] for estudiante in estudiantes if estudiante['nombre'].startswith('P')]
            self.wfile.write(json.dumps({"nombres que inician con P": nombres_con_P}).encode('utf-8'))
        elif self.path == '/contar_carreras':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            carreras = [carrera['carrera'] for carrera in estudiantes]            
            self.wfile.write(json.dumps({"carreras": carreras}).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()