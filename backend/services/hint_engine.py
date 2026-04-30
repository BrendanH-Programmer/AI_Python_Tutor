def generate_hint(error_info, hint_level: int):

    # Accept both single error OR ranked list
    if isinstance(error_info, list):
        errors = error_info
    else:
        errors = [error_info]

    # No errors
    if not errors or not errors[0].get("has_error"):
        return "No issues detected. Your code looks good!"

    # Clamp level
    hint_level = max(1, min(hint_level, 3))

    # Use highest priority error (ranked system)
    primary_error = errors[0]

    error_type = primary_error.get("error_type", "UnknownError")
    message = primary_error.get("message", "")

    # ------------------------
    # LEVEL 1 (high-level intuition)
    # ------------------------
    if hint_level == 1:

        if len(errors) > 1:
            return (
                f"Your code has multiple issues. "
                f"The most important one should be fixed first."
            )

        return (
            "There is an issue in your code. "
            "Think about what might prevent it from running correctly."
        )

    # ------------------------
    # LEVEL 2 (guided learning)
    # ------------------------
    if hint_level == 2:

        readable = error_type.replace("Error", "").replace("_", " ").strip()

        if len(errors) > 1:
            return (
                f"You have multiple issues. "
                f"The highest priority issue is related to a {readable}."
            )

        return (
            f"This looks like a {readable} issue. "
            f"Think about why Python might behave this way."
        )

    # ------------------------
    # LEVEL 3 (explicit teaching)
    # ------------------------
    if hint_level == 3:

        if len(errors) > 1:
            return (
                f"Primary issue: {error_type} → {message}\n"
                f"There are {len(errors) - 1} additional issue(s). "
                f"Fix the highest priority error first, because lower-priority issues may disappear once it is resolved."
            )

        return f"{error_type}: {message}"

    return "Try reviewing your code carefully."