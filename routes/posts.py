from flask import Blueprint, request, jsonify
from py2neo import Node, Relationship
from config import graph

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    user = graph.evaluate("MATCH (u:User {email: $email}) RETURN u", email=data["user_email"])
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    post = Node("Post", title=data["title"], content=data["content"], created_at=data["created_at"])
    graph.create(post)
    graph.create(Relationship(user, "CREATED", post))

    return jsonify({"message": "Post créé", "post": data}), 201
