import requests
url = "http://localhost:8000"

lista_posts = url + "/lista"
get_response = requests.get(url=lista_posts)
print(get_response.text)

lista_posts = url + "/post/2"
get_response = requests.get(url=lista_posts)
print(get_response.text)


url_posts = url + "/posts"
new_post = {
        "title" : "Mi experiencia como dev",
        "content": "Analizando",
}
post_response = requests.post(url=url_posts, data=new_post)

lista_posts = url + "/lista"
get_response = requests.get(url=lista_posts)
print(get_response.text)

url_posts = url + "/post/3"
new_post = {
        "content": "En progreso",
}
post_response = requests.put(url=url_posts, data=new_post)

lista_posts = url + "/lista"
get_response = requests.get(url=lista_posts)
print(get_response.text)

url_posts = url + "/post/2"
post_response = requests.delete(url=url_posts)

lista_posts = url + "/lista"
get_response = requests.get(url=lista_posts)
print(get_response.text)
