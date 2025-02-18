from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Datos de ejemplo
data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]
}

@app.route('/users', methods=['GET'])
def get_users():
    """Retorna la lista de usuarios."""
    return jsonify(data['users'])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retorna un usuario específico por ID."""
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if user is not None:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar el estado del servicio."""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
