from flask import Blueprint, request, jsonify
from data import users, books
from flags import FLAGS

api = Blueprint("api", __name__)



@api.route("/status", methods=["GET"])
def status():
    return jsonify({
        "service": "BookHaven API",
        "version": "1.2.3",
        "environment": "development",
        "maintainer": "bookhaven-team",
        "debug": {
            "last_restart": "2025-01-12 10:32:11",
            "note": "temporary debug enabled",
            "flag": "FLAG{silence_speaks_loudest}"
        }
    })


@api.route("/login", methods=["POST"])
def login():
    data = request.json or {}
    email = data.get("email")
    password = data.get("password")

    # Flag condition: email present, password missing entirely
    if email and password is None:
        return jsonify({
            "status": "success",
            "message": "Logged in as admin",
            "flag": FLAGS["login_bypass"]
        })

    if not email:
        return jsonify({"error": "Email required"}), 400

    # Normal login (would check password in real app)
    return jsonify({
        "status": "success",
        "message": "Login successful"
    })

@api.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@api.route("/checkout", methods=["POST"])
def checkout():
    data = request.json or {}

    items = data.get("items", [])
    total = data.get("total")

    if total is None:
        return jsonify({
            "status": "error",
            "message": "Total missing"
        }), 400

  
    if total <= 1:
        return jsonify({
            "status": "success",
            "message": "Order placed successfully",
            "paid": total,
            "debug_receipt": FLAGS["free_checkout"]
        })

    return jsonify({
        "status": "success",
        "message": "Order placed successfully",
        "paid": total
    })


@api.route("/book", methods=["GET"])
def get_book():
    book_id = request.args.get("id")
    try:
        # Intentionally convert without validation
        idx = int(book_id)
        if idx < 0 or idx >= len(books):
            return jsonify({"error": "Book not found"}), 404
        return jsonify(books[idx])
    except Exception as e:
        # Mishandling: leaking debug flag in error response
        return jsonify({
            "error": str(e),
            "debug_trace": FLAGS["admin_access"]
        }), 500

