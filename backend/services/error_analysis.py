def analyse_code(code):
    try:
        # Try to compile the code (detect syntax errors)
        compiled_code = compile(code, "<string>", "exec")

        # Try to execute safely (detect runtime errors)
        exec_globals = {}
        exec(compiled_code, exec_globals)

        return {
            "type": "none",
            "message": "No errors detected"
        }

    except SyntaxError as e:
        return {
            "type": "SyntaxError",
            "message": str(e),
            "line": e.lineno
        }

    except Exception as e:
        return {
            "type": type(e).__name__,
            "message": str(e)
        }