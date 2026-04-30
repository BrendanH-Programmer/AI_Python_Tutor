def rank_errors(errors, code: str):
    """
    Dynamically ranks errors based on severity, type, and context.
    Returns a sorted list with priority scores.
    """

    ranked = []

    for err in errors:
        error_type = err.get("error_type", "UnknownError")
        message = err.get("message", "")

        score = 0
        reason = []

        # -------------------------
        # 1. SEVERITY BASE SCORE
        # -------------------------
        if error_type in ["SyntaxError", "IncompleteCode", "InvalidSyntax", "MissingSyntax"]:
            score += 100
            reason.append("Blocks execution (syntax level)")

        elif error_type in ["NameError", "TypeError"]:
            score += 70
            reason.append("Runtime logic issue")

        elif error_type in ["ZeroDivisionError"]:
            score += 60
            reason.append("Runtime crash condition")

        else:
            score += 40
            reason.append("General runtime issue")

        # -------------------------
        # 2. CONTEXT ANALYSIS
        # -------------------------
        if "print" in code and "SyntaxError" in error_type:
            score += 10
            reason.append("Common beginner print syntax mistake")

        if "(" in message or ")" in message:
            score += 5
            reason.append("Bracket-related issue detected")

        # -------------------------
        # 3. FREQUENCY BOOST (heuristic)
        # -------------------------
        if "unexpected EOF" in message.lower():
            score += 20
            reason.append("Common incomplete code mistake")

        # -------------------------
        # BUILD RANKED OBJECT
        # -------------------------
        ranked.append({
            "error_type": error_type,
            "message": message,
            "score": score,
            "reason": reason
        })

    # Sort by priority (highest first)
    ranked.sort(key=lambda x: x["score"], reverse=True)

    # Add final ranking index
    for i, err in enumerate(ranked):
        err["priority"] = i + 1

    return ranked