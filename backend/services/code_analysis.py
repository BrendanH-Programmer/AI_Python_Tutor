import ast


def run_code_safely(code: str):

    try:
        tree = ast.parse(code)

        issues = []

        for node in ast.walk(tree):

            # Detect imports (safe informational only)
            if isinstance(node, ast.Import):
                issues.append({
                    "error_type": "ImportUsage",
                    "message": "Module import detected (this is valid Python)",
                })

            if isinstance(node, ast.ImportFrom):
                issues.append({
                    "error_type": "ImportUsage",
                    "message": "From-import detected (valid Python syntax)",
                })

        return {
            "issues": issues
        }

    except SyntaxError as e:
        return {
            "issues": [{
                "error_type": "SyntaxError",
                "message": str(e)
            }]
        }