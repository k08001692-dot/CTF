from flask import Flask
from flask_cors import CORS
from routes import api


app = Flask(__name__)
CORS(app)  # allow frontend to talk to backend

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
