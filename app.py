from flask import Flask
from routes.users import users_bp  # Import des routes

app = Flask(__name__)

# Enregistrer les blueprints (routes)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
