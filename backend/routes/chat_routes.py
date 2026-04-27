from flask import Blueprint, request, jsonify
from services.error_analysis import analyse_code
from services.runtime_analysis import run_code_safely
from services.hint_engine import generate_hint

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    code = data.get("code", "")
    hint_level = data.get("hint_level", 1)

    if not code:
        return jsonify({"error": "No code provided"}), 400

    # 1. Syntax check
    error_info = analyse_code(code)

    # 2. Runtime check (only if syntax is ok)
    runtime_info = None
    if not error_info["has_error"]:
        runtime_info = run_code_safely(code)

    # 3. Decide final error state
    final_error = error_info

    if runtime_info and runtime_info.get("runtime_error"):
        final_error = {
            "has_error": True,
            "error_type": "RuntimeError",
            "message": runtime_info["message"]
        }

    # 4. Generate hint
    hint = generate_hint(final_error, hint_level)

    return jsonify({
        "error": final_error,
        "hint": hint
    })