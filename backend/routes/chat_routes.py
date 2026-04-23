from flask import Blueprint, request, jsonify
from services.error_analysis import analyse_code
from services.hint_engine import generate_hint

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    
    code = data.get("code", "")
    hint_level = data.get("hint_level", 1)

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Step 1: Analyse code
    error_info = analyse_code(code)

    # Step 2: Generate hint
    hint = generate_hint(error_info, hint_level)

    return jsonify({
        "error": error_info,
        "hint": hint
    })