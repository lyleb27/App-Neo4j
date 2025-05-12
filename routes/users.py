from flask import Blueprint, request, jsonify
from py2neo import Node
from config import graph

users_bp = Blueprint('users', __name__)

# Route GET /users pour récupérer tous les utilisateurs
@users_bp.route('/users', methods=['GET'])
def get_users():
    query = "MATCH (u:User) RETURN u"
    users = graph.run(query).data()
    return jsonify(users)

# Route POST /users pour créer un nouvel utilisateur
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    query = "CREATE (u:User {name: $name, email: $email, created_at: timestamp()}) RETURN u"
    user = graph.run(query, name=data["name"], email=data["email"]).data()
    return jsonify(user)
