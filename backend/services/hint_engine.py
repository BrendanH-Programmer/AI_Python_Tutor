def generate_hint(error_info, hint_level):
    error_type = error_info.get("type")
    message = error_info.get("message", "")

    if error_type == "No Error":
        return "Your code looks correct. Try testing different inputs."

    # LEVEL 1: General hint
    if hint_level == 1:
        return "There may be a syntax issue in your code. Check the structure carefully."

    # LEVEL 2: Direction hint
    elif hint_level == 2:
        if error_type == "SyntaxError":
            return f"Check line {error_info.get('line')} for a syntax issue."
        return "Something is wrong in how your code is written."

    # LEVEL 3: Specific hint
    elif hint_level == 3:
        return f"Python says: {message}"

    return "Try reviewing your code again."