import traceback

def run_code_safely(code: str):
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

    except Exception as e:
        return {
            "runtime_error": True,
            "error_type": type(e).__name__,
            "message": str(e)
        }