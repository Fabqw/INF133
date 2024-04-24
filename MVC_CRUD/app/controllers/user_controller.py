from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User
from datetime import datetime

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/users", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form['email']
        password = request.form['password']
        date_nac = request.form['date_nac']
        date_nace = datetime.strptime(date_nac, '%Y-%m-%d').date()
        
        user = User(first_name, last_name, email, password, date_nace)
        user.save()
        return redirect(url_for("user.usuarios"))
    return user_view.registro()


# Actualizar la información de un usuario por su id
# primero recuperamos la información del usuario
@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):
    # Obtenemos el usuario por su id
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    return user_view.actualizar(user)


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@user_bp.route("/users/<int:id>", methods=["POST"])
def actualizar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    # Obtenemos los datos del formulario
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form['email']
    password = request.form['password']
    date_nac = request.form['date_nac']
    date_nace = datetime.strptime(date_nac, '%Y-%m-%d').date()
    # Actualizamos los datos del usuario
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = password
    user.date_nac = date_nace
    # Guardamos los cambios
    user.update()
    return redirect(url_for("user.usuarios"))

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def eliminar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.usuarios"))  # Corregido "usarios" a "usuarios"
