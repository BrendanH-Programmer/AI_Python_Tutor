import traceback

def run_code_safely(code: str):
    """
    Executes code and captures runtime errors.
    Limited builtins for safety.
    """

    try:
        safe_globals = {
            "__builtins__": {
                "print": print,
                "range": range,
                "len": len
            }
        }

        local_vars = {}

        exec(code, safe_globals, local_vars)

        return {
            "runtime_error": False,
            "output": "Code executed successfully"
        }

    except Exception:
        return {
            "runtime_error": True,
            "message": traceback.format_exc()
        }