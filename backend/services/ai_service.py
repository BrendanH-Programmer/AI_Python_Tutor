import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_explanation(code, issues):
    try:

        # Ensure list format
        if isinstance(issues, dict):
            issues = [issues]

        # -------------------------
        # Build structured issue list
        # -------------------------
        issue_text = ""

        for i, issue in enumerate(issues, 1):
            issue_text += f"""
{i}. Type: {issue.get('error_type')}
   Message: {issue.get('message')}
   Priority: {issue.get('priority', 'N/A')}
   Reason: {issue.get('reason', [])}
"""

        prompt = f"""
You are an expert AI Python tutor.

You are helping a beginner understand debugging.

IMPORTANT:
- These are NOT all runtime errors.
- They are ranked learning issues (syntax, logic, warnings).

---

Student Code:
{code}

---

Ranked Issues (highest priority first):
{issue_text}

---

You MUST explain:

1. Overall Summary of the problem
2. Error / Issue Breakdown Table:
   - Type
   - Meaning
   - Why it has this priority
3. Why this ranking order matters for debugging
4. Step-by-step fix plan
5. Final corrected code (if applicable)

Keep explanations simple, beginner-friendly, and educational.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly Python tutor that teaches debugging and ranking of issues clearly."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"