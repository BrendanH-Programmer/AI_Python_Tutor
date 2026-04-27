def generate_hint(error_info, hint_level: int):

    if not error_info["has_error"]:
        return "No issues detected. Your code looks good!"

    hint_level = max(1, min(hint_level, 3))

    error_type = error_info["error_type"]
    message = error_info["message"]

    # SYNTAX ERRORS
    if error_type in ["SyntaxError", "InvalidSyntax", "IncompleteCode"]:

        if hint_level == 1:
            return "There is a syntax issue. Python cannot understand the structure."

        if hint_level == 2:
            return "Check for missing brackets, colons, or incomplete statements."

        if hint_level == 3:
            return f"Exact issue: {message}"

    # RUNTIME ERRORS
    if error_type == "RuntimeError":

        if hint_level == 1:
            return "Your code ran but crashed during execution."

        if hint_level == 2:
            return "Check operations like division, variable names, or loops."

        if hint_level == 3:
            return f"Runtime error details: {message}"

    return "Try reviewing your code carefully."