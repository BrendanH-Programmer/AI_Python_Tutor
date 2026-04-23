def analyse_code(code):
    try:
        compile(code, "<string>", "exec")
        return {
            "type": "No Error",
            "message": "Code executed successfully"
        }
    except SyntaxError as e:
        return {
            "type": "SyntaxError",
            "message": str(e),
            "line": e.lineno
        }
    except Exception as e:
        return {
            "type": "RuntimeError",
            "message": str(e)
        }