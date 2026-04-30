from flask import Blueprint, request, jsonify
from services.error_analysis import analyse_code
from services.code_analysis import run_code_safely
from services.error_ranker import rank_errors
from services.hint_engine import generate_hint
from services.ai_service import get_ai_explanation

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
    # 1. Syntax Analysis
    # -------------------------
    syntax_result = analyse_code(code)

    # -------------------------
    # 2. Static Analysis (NOT runtime execution)
    # -------------------------
    runtime_result = run_code_safely(code)

    # -------------------------
    # 3. Collect ALL issues
    # -------------------------
    issues = []

    if syntax_result.get("has_error"):
        issues.append({
            "error_type": syntax_result.get("error_type"),
            "message": syntax_result.get("message"),
            "category": "error"
        })

    for issue in runtime_result.get("issues", []):
        issues.append({
            "error_type": issue.get("error_type"),
            "message": issue.get("message"),
            "category": "warning"
        })

    # -------------------------
    # 4. Rank issues
    # -------------------------
    ranked_issues = rank_errors(issues, code) if issues else []

    # -------------------------
    # 5. Top issue for hints
    # -------------------------
    top_issue = ranked_issues[0] if ranked_issues else {
        "error_type": None,
        "message": "No issues",
        "has_error": False
    }

    hint_input = {
        "has_error": len(issues) > 0,
        "error_type": top_issue.get("error_type"),
        "message": top_issue.get("message")
    }

    # -------------------------
    # 6. Hint system
    # -------------------------
    hint = generate_hint(hint_input, hint_level)

    # -------------------------
    # 7. AI explanation (level 3 only)
    # -------------------------
    ai_explanation = None

    if hint_level >= 3 and ranked_issues:
        ai_explanation = get_ai_explanation(code, ranked_issues)

    # -------------------------
    # 8. Response
    # -------------------------
    return jsonify({
        "success": True,
        "code_received": code,
        "issues": ranked_issues,
        "hint": hint,
        "ai_explanation": ai_explanation,
        "hint_level_used": max(1, min(hint_level, 3))
    })