from flask import Blueprint, request, jsonify
from data import users, books
from flags import FLAGS

api = Blueprint("api", __name__)



@api.route("/api/status", methods=["GET"])
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

@api.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

from flags import FLAGS

@api.route("/api/checkout", methods=["POST"])
def checkout():
    data = request.json or {}

    items = data.get("items", [])
    total = data.get("total")

    if total is None:
        return jsonify({
            "status": "error",
            "message": "Total missing"
        }), 400

    # 🔥 Flag 4 condition
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


