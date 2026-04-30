from flask import Blueprint, request, jsonify
from services.error_analysis import analyse_code
from services.runtime_analysis import run_code_safely
from services.hint_engine import generate_hint
from services.ai_service import get_ai_explanation
from services.error_ranker import rank_errors

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

    # -------------------------
    # 1. Syntax analysis
    # -------------------------
    syntax_result = analyse_code(code)

    # -------------------------
    # 2. Runtime analysis
    # -------------------------
    runtime_result = None
    if not syntax_result["has_error"]:
        runtime_result = run_code_safely(code)

    # -------------------------
    # 3. Collect errors
    # -------------------------
    errors = []

    if syntax_result["has_error"]:
        errors.append(syntax_result)

    if runtime_result and runtime_result.get("runtime_error"):
        errors.append({
            "has_error": True,
            "error_type": runtime_result.get("error_type", "RuntimeError"),
            "message": runtime_result.get("message", "Unknown runtime error")
        })

    # -------------------------
    # 4. Rank errors
    # -------------------------
    ranked_errors = rank_errors(errors, code) if errors else []

    # -------------------------
    # 5. Select TOP error (by rank)
    # -------------------------
    top_error = ranked_errors[0] if ranked_errors else {
        "has_error": False,
        "error_type": None,
        "message": "No errors"
    }

    # Convert ranked format → hint format
    hint_input = {
        "has_error": len(errors) > 0,
        "error_type": top_error.get("error_type"),
        "message": top_error.get("message")
    }

    # -------------------------
    # 6. Generate hint
    # -------------------------
    hint = generate_hint(hint_input, hint_level)

    # -------------------------
    # 7. AI explanation (level 3 only)
    # -------------------------
    ai_explanation = None

    if hint_level >= 3 and ranked_errors:

        # Build explanation-friendly structure
        structured_errors = []

        for err in ranked_errors:
            structured_errors.append({
                "type": err.get("error_type"),
                "message": err.get("message"),
                "priority": err.get("priority"),
                "score": err.get("score"),
                "reason": err.get("reason", [])
            })

        ai_explanation = get_ai_explanation(code, structured_errors)

    # -------------------------
    # 8. Response
    # -------------------------
    return jsonify({
        "success": True,
        "code_received": code,
        "errors": ranked_errors,
        "hint": hint,
        "ai_explanation": ai_explanation,
        "hint_level_used": max(1, min(hint_level, 3))
    })