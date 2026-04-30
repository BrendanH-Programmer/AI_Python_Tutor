import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_explanation(code, errors):
    try:

        # If only one error comes in, normalize it
        if isinstance(errors, dict):
            errors = [errors]

        # Build error section for prompt
        error_text = ""

        if not errors:
            error_text = "No errors detected."
        else:
            for i, err in enumerate(errors, 1):
                error_type = err.get("error_type", "UnknownError")
                message = err.get("message", "No message provided")
                error_text += f"\n{i}. {error_type}: {message}"

        prompt = f"""
You are an expert AI Python tutor.

Your job is to:
1. Explain ALL errors clearly
2. Explain WHY they are ranked in this order
3. Teach the student how to think about debugging order

Student code:
{code}

Ranked errors (highest priority first):

{errors}

---

IMPORTANT TEACHING RULE:

You MUST explain:

A) What each error means
B) Why it has its priority level
C) Why higher priority errors must be fixed first

Use this structure:

1. Overall Problem Summary
2. Error Breakdown Table (IMPORTANT)
   - Error Type
   - Meaning
   - Why it has this priority
3. Why This Order Matters (VERY IMPORTANT SECTION)
4. Step-by-step Fix Plan
5. Final Corrected Code
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a friendly Python tutor that explains errors clearly and prioritises fixes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"