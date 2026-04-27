from flask import Blueprint, request, jsonify
from services.error_analysis import analyse_code
from services.runtime_analysis import run_code_safely
from services.hint_engine import generate_hint

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    code = data.get("code")
    hint_level = data.get("hint_level", 1)

    if not code:
        return jsonify({
            "success": False,
            "error": "No code provided"
        }), 400

    # 1. Syntax analysis
    syntax_result = analyse_code(code)

    # 2. Runtime analysis (only if syntax OK)
    runtime_result = None
    if not syntax_result["has_error"]:
        runtime_result = run_code_safely(code)

    # 3. Determine final error state
    final_error = syntax_result

    if runtime_result and runtime_result.get("runtime_error"):
        final_error = {
            "has_error": True,
            "error_type": "RuntimeError",
            "message": runtime_result["message"]
        }

    # 4. Generate hint
    hint = generate_hint(final_error, hint_level)

    return jsonify({
        "success": True,
        "code_received": code,
        "error": final_error,
        "hint": hint,
        "hint_level_used": max(1, min(hint_level, 3))
    })