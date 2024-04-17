from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Fabricio",
        "apellido": "Quispe",
        "carrera": "Ingenieria de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Pedro",
        "apellido": "Lima",
        "carrera": "Ingenieria de software",
    },
    {
        "id": 3,
        "nombre": "Pepe",
        "apellido": "Lima",
        "carrera": "Ingenieria de software",
    },
    {
        "id": 4,
        "nombre": "Carla",
        "apellido": "Loza",
        "carrera": "Ingenieria de software",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == "/eliminar_estudiante":
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
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
            # cnt_carreras = carreras.count('Ingeniería de software')
            cnt_carreras = {}
            for carrera in carreras:
                if carrera in cnt_carreras:
                    cnt_carreras[carrera] += 1
                else:
                    cnt_carreras[carrera] = 1            
            self.wfile.write(json.dumps({"alumnos por carrera": cnt_carreras}).encode('utf-8'))
        elif self.path == '/total_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            #estudiantes = [estudiante for estudiante in estudiantes]
            cnt_estudiantes = len(estudiantes)
            self.wfile.write(json.dumps({"estudiantes totales": cnt_estudiantes}).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/actualizar_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            id = post_data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(post_data)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
            
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