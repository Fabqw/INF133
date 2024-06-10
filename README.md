# INF-133

## Repositorio de lo Avanzados y Practicas
-   Estudiante: Fernando Fabricio Quispe Yujra

### Prácticas
-   servidor SOAP
-   servidor REST
-   servidor RESTful
-   servidor GRAPHQL
-   servidor CRUD
-   servidor MVC

### Codigos importantes
-   .\venv\Scripts\activate (Activar el entrono virtual)
-   Set-ExecutionPolicy Unrestricted -Scope Process  (Poder ejercutar scripts)
-   ...

### metodos REST

#### do_GET
obtener informacion
es heredado de BaseHTTPRequestHandler
.send_response(200) es success correcta
.send_response(404) page not fount error de peticion

#### do_POST
publicar algo
.send_response(201) se a insertado(publicar) el valor de forma correcta


#### Error de cliene 4xx
-   400 error de cliente
-   401 error de permisos
-   404 no se encontro en el servidor

## Tipo de APIs
API RESTful
-   uso correcto de verbos
-   uso de sustantivos en end points y nombres en plural
-   diseño de URL con patrones logicos

## Despliegue
- mandar una solucion a un entorno
- se lo realizo en digitalocean
1. fases de despliegue: 
    - preparacion
    - implementacion
    - pruebas
    - monitore
    - mantenimiento




