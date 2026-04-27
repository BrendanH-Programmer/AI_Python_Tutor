def generate_hint(error_info, hint_level: int):

    if not error_info.get("has_error"):
        return "No issues detected. Your code looks good!"

    # Clamp hint level (1–3)
    hint_level = max(1, min(hint_level, 3))

    error_type = error_info.get("error_type", "UnknownError")
    message = error_info.get("message", "")

    # ------------------------
    # HINT LEVEL 1 (very vague)
    # ------------------------
    if hint_level == 1:
        return "There is an issue in your code. Try reviewing it carefully."

    # ------------------------
    # HINT LEVEL 2 (guided)
    # ------------------------
    elif hint_level == 2:

        # Convert error type into readable words
        readable_error = error_type.replace("Error", "").replace("_", " ").strip()

        return f"This looks like a {readable_error.lower()} issue. Think about what might cause it."

    # ------------------------
    # HINT LEVEL 3 (explicit)
    # ------------------------
    elif hint_level == 3:

        return f"{error_type}: {message}"

    return "Try reviewing your code carefully."