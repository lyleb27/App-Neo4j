from flask import Blueprint, request, jsonify
from py2neo import Node, Relationship
from config import graph

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = Node("User", name=data["name"], email=data["email"], created_at=data["created_at"])
    graph.create(user)
    return jsonify({"message": "Utilisateur créé", "user": data}), 201

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = graph.run("MATCH (u:User) RETURN u.name, u.email").data()
    return jsonify(users)

@users_bp.route('/users/<email>', methods=['GET'])
def get_user(email):
    user = graph.run("MATCH (u:User {email: $email}) RETURN u", email=email).data()
    return jsonify(user) if user else ("Utilisateur non trouvé", 404)
