def test_get_animals(test_client, auth_headers):
    response = test_client.get("/api/animals", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Lion"


def test_get_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"


def test_update_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json["species"] == "Loxodonta africana"
    assert response.json["age"] == 12


def test_delete_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 204

    # Verifica que el animal ha sido eliminado
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 404

# Para los usuarios

def test_get_animals(test_client, user_auth_headers):
    response = test_client.get("/api/animals", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []

def test_get_animal(test_client, auth_headers, user_auth_headers):
    # Primero crea un animal con un administrador
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 201
    animal_id = response.json["id"]

    # Ahora obtén el animal con un usuario
    response = test_client.get(f"/api/animals/{animal_id}", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Tiger"

def test_create_animal_user_restricted(test_client, user_auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"

def test_update_animal_user_restricted(test_client, user_auth_headers):
    # Primero crea un animal con un administrador
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"
    animal_id = response.json["id"]

    # Ahora intenta actualizar el animal con un usuario
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=user_auth_headers
    )
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"

def test_delete_animal_user_restricted(test_client, user_auth_headers):
    # Primero crea un animal con un administrador
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"
    animal_id = response.json["id"]

    # Ahora intenta eliminar el animal con un usuario
    response = test_client.delete(f"/api/animals/{animal_id}", headers=user_auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"