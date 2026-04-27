import ast

def analyse_code(code: str):
    """
    Very simple Python error detection using AST parsing.
    Later we can upgrade to deeper static analysis.
    """

    try:
        ast.parse(code)
        return {
            "has_error": False,
            "error_type": None,
            "message": "No syntax errors detected"
        }

    except SyntaxError as e:
        return {
            "has_error": True,
            "error_type": "SyntaxError",
            "message": str(e),
            "line": e.lineno
        }

    except Exception as e:
        return {
            "has_error": True,
            "error_type": "Error",
            "message": str(e)
        }