import traceback

def run_code_safely(code: str):
    """
    Executes code safely and captures runtime errors.
    WARNING: This is still basic (we improve later with sandboxing).
    """

    try:
        # Safe execution environment
        local_vars = {}

        exec(code, {"__builtins__": {}}, local_vars)

        return {
            "runtime_error": False,
            "output": local_vars
        }

    except Exception:
        return {
            "runtime_error": True,
            "message": traceback.format_exc()
        }