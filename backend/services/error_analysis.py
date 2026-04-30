import ast


def analyse_code(code: str):
    """
    Analyses Python code for syntax errors using AST parsing.
    Returns structured error format compatible with multi-error system.
    """

    try:
        ast.parse(code)

        return {
            "has_error": False,
            "error_type": None,
            "message": "No syntax errors"
        }

    except SyntaxError as e:

        msg = str(e)

        # Classify syntax error type
        if "unexpected EOF" in msg:
            error_type = "IncompleteCode"

        elif "invalid syntax" in msg:
            error_type = "InvalidSyntax"

        elif "expected" in msg:
            error_type = "MissingSyntax"

        else:
            error_type = "SyntaxError"

        return {
            "has_error": True,
            "error_type": error_type,
            "message": msg,
            "line": e.lineno,
            "column": e.offset,
            "text": e.text
        }