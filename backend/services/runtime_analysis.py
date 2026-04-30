import traceback
import io
import sys


def run_code_safely(code: str):
    try:
        # Capture print output
        output_buffer = io.StringIO()
        sys.stdout = output_buffer

        safe_globals = {
            "__builtins__": {
                "print": print,
                "range": range,
                "len": len,
                "int": int,
                "str": str,
                "float": float
            }
        }

        local_vars = {}

        exec(code, safe_globals, local_vars)

        output = output_buffer.getvalue()

        sys.stdout = sys.__stdout__

        return {
            "runtime_error": False,
            "output": output.strip() if output else "Code executed successfully"
        }

    except Exception as e:
        sys.stdout = sys.__stdout__

        return {
            "runtime_error": True,
            "error_type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }