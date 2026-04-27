def generate_hint(error_info, hint_level):
    error_type = error_info.get("type")
    message = error_info.get("message", "")

    # NO ERROR
    if error_type == "none":
        return "Your code ran successfully. Try adding more complexity or testing edge cases."

    # SYNTAX ERRORS
    if error_type == "SyntaxError":

        if ":" in message:
            return [
                "Check if you are missing a colon ':' in statements like if, for, or def.",
                "Python requires a colon at the end of control statements.",
                "Add ':' at the end of your statement (e.g. if x == 5:)"
            ][min(hint_level-1, 2)]

        if "unexpected EOF" in message:
            return [
                "It looks like something is incomplete.",
                "Check if all brackets or quotes are properly closed.",
                "You are likely missing a closing bracket or quotation mark."
            ][min(hint_level-1, 2)]

        return [
            "Check your syntax carefully.",
            "Focus on the line mentioned in the error.",
            f"Review line {error_info.get('line')} for syntax issues."
        ][min(hint_level-1, 2)]

    # ZERO DIVISION
    if error_type == "ZeroDivisionError":
        return [
            "Check your division operations.",
            "You might be dividing a number by zero.",
            "Division by zero is not allowed — ensure denominator is not 0."
        ][min(hint_level-1, 2)]

    # NAME ERROR
    if error_type == "NameError":
        return [
            "Check variable names.",
            "A variable might not be defined.",
            "Define the variable before using it."
        ][min(hint_level-1, 2)]

    # TYPE ERROR
    if error_type == "TypeError":
        return [
            "Check the types of your variables.",
            "You may be mixing incompatible types.",
            "Ensure operations are between compatible data types."
        ][min(hint_level-1, 2)]

    # FALLBACK
    return f"Error detected: {message}"