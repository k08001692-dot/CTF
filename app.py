import os
from flask import Flask
from flask_cors import CORS
from routes import api


app = Flask(__name__)

# Allow cross-origin requests from any origin to /api/*
CORS(app, resources={r"/api/*": {"origins": "*"}})

# All API routes are mounted under /api
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
