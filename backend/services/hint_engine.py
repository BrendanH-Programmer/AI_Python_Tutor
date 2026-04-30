def generate_hint(error_info, hint_level: int):

    # Allow both single error OR list of errors
    if isinstance(error_info, list):
        errors = error_info
    else:
        errors = [error_info]

    # No errors case
    if not errors or not errors[0].get("has_error"):
        return "No issues detected. Your code looks good!"

    # Clamp hint level
    hint_level = max(1, min(hint_level, 3))

    # Use first (most important) error for hint system
    primary_error = errors[0]

    error_type = primary_error.get("error_type", "UnknownError")
    message = primary_error.get("message", "")

    # ------------------------
    # LEVEL 1 (very vague)
    # ------------------------
    if hint_level == 1:
        if len(errors) > 1:
            return f"There are {len(errors)} issues in your code. Try to find the first problem."
        return "There is an issue in your code. Try reviewing it carefully."

    # ------------------------
    # LEVEL 2 (guided)
    # ------------------------
    if hint_level == 2:
        readable_error = error_type.replace("Error", "").replace("_", " ").strip().lower()

        if len(errors) > 1:
            return f"There are multiple issues. The first one looks like a {readable_error} problem."

        return f"This looks like a {readable_error} issue. Think about what might cause it."

    # ------------------------
    # LEVEL 3 (explicit)
    # ------------------------
    if hint_level == 3:

        if len(errors) > 1:
            extra = f"\nAlso: {len(errors) - 1} more issue(s) detected."
            return f"{error_type}: {message}{extra}"

        return f"{error_type}: {message}"

    return "Try reviewing your code carefully."