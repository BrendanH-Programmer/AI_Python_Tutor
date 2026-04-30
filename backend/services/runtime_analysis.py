import ast

def run_code_safely(code: str):
    """
    NOTE: This is no longer execution.
    This is static analysis only (like ChatGPT / VS Code warnings).
    """

    try:
        tree = ast.parse(code)

        issues = []

        for node in ast.walk(tree):

            # Detect imports (SAFE - NOT execution)
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                issues.append({
                    "error_type": "ImportStatement",
                    "message": "This code imports external modules",
                    "note": "No execution performed"
                })

        return {
            "runtime_error": len(issues) > 0,
            "issues": issues
        }

    except SyntaxError as e:
        return {
            "runtime_error": True,
            "error_type": "SyntaxError",
            "message": str(e)
        }