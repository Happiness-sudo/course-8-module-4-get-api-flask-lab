from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome"}), 200


@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        filtered = [
            p for p in products
            if p["category"].lower() == category.lower()
        ]
        return jsonify(filtered), 200

    return jsonify(products), 200


@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    for p in products:
        if p["id"] == id:
            return jsonify(p), 200

    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run()