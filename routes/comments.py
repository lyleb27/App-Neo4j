from flask import Blueprint, request, jsonify
from py2neo import Node, Relationship
from config import graph

comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/posts/<post_id>/comments', methods=['POST'])
def add_comment(post_id):
    data = request.json
    user = graph.evaluate("MATCH (u:User {email: $email}) RETURN u", email=data["user_email"])
    post = graph.evaluate("MATCH (p:Post {title: $title}) RETURN p", title=post_id)

    if not user or not post:
        return jsonify({"error": "Utilisateur ou post non trouvé"}), 404

    comment = Node("Comment", content=data["content"], created_at=data["created_at"])
    graph.create(comment)
    graph.create(Relationship(user, "CREATED", comment))
    graph.create(Relationship(post, "HAS_COMMENT", comment))

    return jsonify({"message": "Commentaire ajouté"}), 201
