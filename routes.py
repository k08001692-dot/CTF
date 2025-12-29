from flask import Blueprint, request, jsonify
from data import users, books, orders, wishlists, sessions
from flags import FLAGS
import hashlib
import time

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


@api.route("/order", methods=["GET"])
def get_order():
    order_id = request.args.get("id")
    if not order_id:
        return jsonify({"error": "Order ID required"}), 400
    try:
        order_id = int(order_id)
    except:
        return jsonify({"error": "Invalid order ID"}), 400
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404


@api.route("/wishlist", methods=["GET"])
def get_wishlist():
    user_id = request.args.get("user_id", type=int)
    if not user_id:
        return jsonify({"error": "User ID required"}), 400
    if user_id in wishlists:
        wl = wishlists[user_id]
        return jsonify({
            "status": "success",
            "count": len(wl.get("items", [])),
            "data": wl
        })
    return jsonify({"status": "success", "count": 0, "items": []})


@api.route("/user/role", methods=["POST"])
def update_role():
    data = request.json or {}
    user_id = data.get("user_id")
    new_role = data.get("role")
    if not user_id or not new_role:
        return jsonify({"error": "user_id and role required"}), 400
    for user in users:
        if user["id"] == user_id:
            if new_role == "admin":
                user["role"] = new_role
                return jsonify({
                    "status": "success",
                    "message": "Role updated",
                    "user": user["email"],
                    "new_role": new_role,
                    "grant_token": FLAGS["role_escalation"]
                })
            user["role"] = new_role
            return jsonify({"status": "success", "message": "Role updated"})
    return jsonify({"error": "User not found"}), 404


@api.route("/profile", methods=["GET"])
def get_profile():
    auth = request.headers.get("Authorization", "")
    if not auth:
        return jsonify({"error": "Authorization required"}), 401
    if auth.startswith("Bearer "):
        token = auth[7:]
        if len(token) > 0:
            if token == "undefined" or token == "null" or token.startswith("{{"): 
                return jsonify({
                    "status": "success",
                    "user": "guest",
                    "debug_token": FLAGS["token_bypass"]
                })
            return jsonify({"status": "success", "user": "authenticated"})
    return jsonify({"error": "Invalid token format"}), 401


@api.route("/admin/reports", methods=["GET"])
def admin_reports():
    auth = request.headers.get("Authorization", "")
    is_admin = request.headers.get("X-Admin", "false")
    user_role = request.args.get("role", "user")
    if is_admin.lower() == "true" or user_role == "admin":
        return jsonify({
            "status": "success",
            "reports": [
                {"id": 1, "type": "sales", "date": "2025-01-01"},
                {"id": 2, "type": "inventory", "date": "2025-01-02"}
            ],
            "admin_key": FLAGS["admin_panel"]
        })
    return jsonify({"error": "Admin access required"}), 403

