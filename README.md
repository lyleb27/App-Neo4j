# App Neo4j

## Description

Ce projet est une API RESTful développée en Python avec Flask, utilisant une base de données Neo4j pour gérer des utilisateurs, des posts et des commentaires.

## Prérequis

- Python 3.8+
- Docker
- Neo4j (via Docker ou installation locale)
- Postman ou curl pour tester l'API

## Installation

1. Clonez le dépôt :
```bash
   git clone https://github.com/lyleb27/App-Neo4j.git
   cd App-Neo4j
```
2. Fichiers :

API-Mongo/ \
│── app.py --> Point d'entrée de l'application Flask\
│── requirements.txt --> Liste des dépendances\
│── config.py --> Configuration de Neo4j\
│── models.py --> Définition des modèles et relations\
│── routes/\
│   │── users.py --> Routes pour les utilisateurs\
│   │── posts.py --> Routes pour les posts\
│   │── comments.py --> Routes pour les commentaires\
│── .gitignore --> Fichiers à ignorer par Git\
│── README.md --> Documentation du projet\
└── docker-compose.yml --> Configuration Docker pour Neo4j\

1. Installez les dépendances :

```bash
pip install -r requirements.txt
```

4. Démarrez le conteneur Docker pour Neo4j

5. Tester les routes :

   - Créer un utilisateur (POST /users)
```bash
curl -X POST http://127.0.0.1:5000/users ^
     -H "Content-Type: application/json" ^
     -d "{\"name\": \"Alice\", \"email\": \"alice@example.com\"}"
```

   - Obtenir la liste des utilisateurs (GET /users)
```bash
curl http://127.0.0.1:5000/users
```

   - Obtenir un utilisateur par ID (GET /users/<id>)
```bash
curl http://127.0.0.1:5000/users/123
Remplace 123 par l’ID réel de l’utilisateur.
```

   - Mettre à jour un utilisateur (PUT /users/<id>)
```bash
curl -X PUT http://127.0.0.1:5000/users/123 ^
     -H "Content-Type: application/json" ^
     -d "{\"name\": \"Alice Updated\"}"
```

   - Supprimer un utilisateur (DELETE /users/<id>)
```bash
curl -X DELETE http://127.0.0.1:5000/users/123
```

   - Créer un post pour un utilisateur (POST /users/<id>/posts)
```bash
curl -X POST http://127.0.0.1:5000/users/123/posts ^
     -H "Content-Type: application/json" ^
     -d "{\"title\": \"Mon premier post\", \"content\": \"Hello Neo4j!\"}"
```

   - Ajouter un commentaire à un post (POST /posts/<id>/comments)
```bash
curl -X POST http://127.0.0.1:5000/posts/456/comments ^
     -H "Content-Type: application/json" ^
     -d "{\"user_id\": \"123\", \"content\": \"Super post !\"}"
```