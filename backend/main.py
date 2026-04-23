from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # register routes
    app.register_blueprint(chat_bp)

    return app


app = create_app()

if __name__ == "__main__":
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True)