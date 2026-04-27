import ast

def analyse_code(code: str):
    try:
        ast.parse(code)

        return {
            "has_error": False,
            "error_type": None,
            "message": "No syntax errors"
        }

    except SyntaxError as e:

        error_type = "SyntaxError"

        # better classification
        msg = str(e)

        if "unexpected EOF" in msg:
            error_type = "IncompleteCode"

        elif "invalid syntax" in msg:
            error_type = "InvalidSyntax"

        return {
            "has_error": True,
            "error_type": error_type,
            "message": msg,
            "line": e.lineno
        }