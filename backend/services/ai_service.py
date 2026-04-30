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
You are an AI Python tutor helping a beginner student.

Student's code:
{code}

The following errors were detected:

{error_text}

Respond in this structure:

1. Simple Explanation (overall issue summary)
2. Why It Happened
3. Step-by-step Fix (in correct order)
4. Final corrected code

Keep explanations beginner-friendly and clear.
Focus on fixing errors in order of importance.
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