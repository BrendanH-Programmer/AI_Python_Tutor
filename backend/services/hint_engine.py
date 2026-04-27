def generate_hint(error_info, hint_level):
    error_type = error_info.get("type")

    # No error
    if error_type == "none":
        return "Your code ran successfully. Try testing edge cases or improving structure."

    # SYNTAX ERRORS
    if error_type == "SyntaxError":
        if hint_level == 1:
            return "Check your syntax carefully. Look for missing brackets, colons, or indentation."
        elif hint_level == 2:
            return "Focus on the line mentioned in the error. Something is not written in valid Python format."
        else:
            return f"The issue is likely near line {error_info.get('line')}. Review that line closely."

    # DIVISION BY ZERO
    if error_type == "ZeroDivisionError":
        if hint_level == 1:
            return "Check any division operations in your code."
        elif hint_level == 2:
            return "A number is being divided by zero, which is not allowed."
        else:
            return "You are dividing by zero. Ensure the denominator is not zero."

    # NAME ERROR
    if error_type == "NameError":
        if hint_level == 1:
            return "Check variable names used in your code."
        elif hint_level == 2:
            return "You may be using a variable that hasn't been defined."
        else:
            return "A variable is being used before it is defined."

    # DEFAULT fallback
    return f"An error occurred: {error_info.get('message')}"