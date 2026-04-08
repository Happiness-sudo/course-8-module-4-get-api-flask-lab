from flask import Flask, jsonify, request

app = Flask(__name__)

#  MOVE DATA HERE (DO NOT IMPORT FROM data.py)
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

"""
    Homepage route that returns a welcome message.

    Returns:
        dict: A JSON response with a welcome message.
    """
/*******  6bc691d5-62e3-4a50-91ce-0ecc3981923c  *******/


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome"}), 200


@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        filtered = []
        for product in products:
            if product["category"].lower() == category.lower():
                filtered.append(product)
        return jsonify(filtered), 200

    return jsonify(products), 200


@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run()