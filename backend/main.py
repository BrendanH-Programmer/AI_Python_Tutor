from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.chat_routes import chat_bp
import os

# Set frontend folder path
app = Flask(__name__, static_folder="../frontend")
CORS(app)

# Register API routes
app.register_blueprint(chat_bp)

print("Flask app created")

# Serve frontend homepage
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

# Serve static files (CSS, JS)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)