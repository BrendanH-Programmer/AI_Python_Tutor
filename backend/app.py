from flask import Flask
from flask_cors import CORS

from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)

@app.route("/")
def home():
    return {"message": "Backend running successfully"}

if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(debug=True, host="127.0.0.1", port=5000)