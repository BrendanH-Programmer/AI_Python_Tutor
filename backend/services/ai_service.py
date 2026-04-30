import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def get_ai_explanation(code, error_info):
    try:
        error_type = error_info.get("error_type")
        message = error_info.get("message")

        prompt = f"""
You are an AI Python tutor helping a beginner student.

Student's code:
{code}

Error:
{error_type}: {message}

Respond in this structure:

1. Simple Explanation (1-2 sentences)
2. Why It Happened
3. How To Fix It (with corrected example code)

Keep explanations beginner-friendly and clear.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a friendly Python tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI error: {str(e)}"