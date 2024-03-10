import requests

# definir la consulat GRAPHQL
query = """ 
    {
        goodbye
    }
"""

url = "http://localhost:8000/graphql"

response = requests.post(url, json={'query': query})
print(response.text)