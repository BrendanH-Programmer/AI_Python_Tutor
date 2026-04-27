def generate_hint(error_info, hint_level: int):
    """
    Tiered hint system:
    Level 1 = general hint
    Level 2 = more specific
    Level 3 = almost answer
    """

    if not error_info["has_error"]:
        return "No issues found — try running your code!"

    error_type = error_info["error_type"]
    message = error_info["message"]

    # Clamp hint level
    hint_level = max(1, min(hint_level, 3))

    if error_type == "SyntaxError":

        if hint_level == 1:
            return "There is a syntax issue in your code. Check your brackets and punctuation."

        if hint_level == 2:
            return "Python cannot parse your code. Look carefully around missing or incorrect symbols."

        if hint_level == 3:
            return f"SyntaxError detected: {message}"

    # fallback
    return "Try reviewing your code step by step."