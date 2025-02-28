from flask import Flask, jsonify

app = Flask(__name__)

# Sample mock data
MOCK_DATA = {
    "users": [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ],
    "products": [
        {"id": 101, "name": "Product A", "price": 99.99},
        {"id": 102, "name": "Product B", "price": 149.99}
    ]
}

@app.route('/')
def index():
    return jsonify({"message": "Mock API Server is running"})

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(MOCK_DATA["users"])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = MOCK_DATA["users"]
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(MOCK_DATA["products"])

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    products = MOCK_DATA["products"]
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
