import requests

# Tester la création d'un utilisateur
url = "http://127.0.0.1:5000/users"
data = {"name": "Alice", "email": "alice@example.com"}
response = requests.post(url, json=data)
print("Création utilisateur:", response.json())

# Tester la récupération des utilisateurs
response = requests.get(url)
print("Liste des utilisateurs:", response.json())
