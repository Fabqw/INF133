from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hola mundo!!!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"Error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = request.args.get("num1") 
    num2 = request.args.get("num2")   
    if not num1 or not num2:
        if not num1:
            return jsonify({"error": "Se requiere un num1 en los parámetros de la URL."}), 400
        if not num2:
            return jsonify({"error": "Se requiere un num2 en los parámetros de la URL."}), 400
    return jsonify({"mensaje": f"la suma es: {int(num1)+int(num2)}"})
    

@app.route("/palindromo")
def palindromo():
    palabra = request.args.get('cadena').lower()
    if not palabra:
        return(
            jsonify({"error": "Se requiere un num1 o num2 en los parámetros de la URL."}),
            400,
        )      
    if palabra == palabra[::-1]:
        return jsonify({"mensaje": f"la cadena es palindromo"})
    return jsonify({"mensaje": f"la cadena no es palindromo"})
            
@app.route("/contar")
def contar():
    palabra = request.args.get('cadena')
    vocal = request.args.get('vocal')
    if not palabra or not vocal or len(vocal) != 1 or vocal.lower() not in 'aeiou':
        return jsonify({"error": "Se requiere una cadena y una vocal válida en los parámetros de la URL."}), 400
    
    palabra = palabra.lower()
    vocal = vocal.lower()
    contador = palabra.count(vocal)
    
    return jsonify({"cantidad": contador}), 200

if __name__ == '__main__':
    app.run()