from flask import Blueprint, request, jsonify

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    code = data.get("code", "")
    hint_level = data.get("hint_level", 1)

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Temporary safe response (NO imports)
    return jsonify({
        "error": "none",
        "hint": f"Received code with hint level {hint_level}"
    })