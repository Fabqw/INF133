from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

# Base de datos simulada de publicaciones
db = {
    1: {
        "title": "Mi primera publicación",
        "content": "HOLA1",
    },
    2: {
        "title": "Otra publicación",
        "content": "HOLA2",
    },
}

class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar las cabeceras de respuesta
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        # Generar la respuesta JSON de acuerdo a la solicitud
        if self.path == "/posts":
            self.wfile.write(json.dumps(list(db.values())).encode())
        elif self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            post = db.get(post_id)
            if post:
                self.wfile.write(json.dumps(post).encode())
            else:
                self.send_error(404, "Publicación no encontrada")
        elif self.path == "/lista":
             posts = list(db.values())
             self.wfile.write(json.dumps(posts).encode())
        else:
            self.send_error(404, "Ruta no válida")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode())

        # Crear una nueva publicación
        if self.path == "/posts":
            title = post_params.get("title", [""])[0]
            content = post_params.get("content", [""])[0]
            new_post_id = max(db.keys()) + 1
            db[new_post_id] = {"title": title, "content": content}
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"id": new_post_id}).encode())
        else:
            self.send_error(404, "Ruta no válida")

    def do_PUT(self):
        # Actualizar una publicación existente
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                post_params = parse_qs(post_data.decode())
                db[post_id]["title"] = post_params.get("title", [db[post_id]["title"]])[
                    0
                ]
                db[post_id]["content"] = post_params.get(
                    "content", [db[post_id]["content"]]
                )[0]
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"id": post_id}).encode())
            else:
                self.send_error(404, "Publicación no encontrada")
        else:
            self.send_error(404, "Ruta no válida")

    def do_DELETE(self):
        # Eliminar una publicación existente
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                del db[post_id]
                self.send_response(204)
                self.end_headers()
            else:
                self.send_error(404, "Publicación no encontrada")
        else:
            self.send_error(404, "Ruta no válida")


def run_server(server_class=HTTPServer, handler_class=BlogHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor web en http://localhost:{port}/")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()