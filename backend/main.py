from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)

print("Flask app created")

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)