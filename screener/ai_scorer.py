import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

def score_resume(resume_text, job_description):
    model = genai.GenerativeModel('gemini-3.6-flash')

    prompt = f"""
You are an expert technical recruiter. Compare the following resume against the job description.

Job Description:
{job_description}

Resume:
{resume_text}

Respond ONLY in valid JSON format, with no extra text, no markdown formatting, exactly like this:
{{
    "score": <a number from 0 to 100 representing how well the resume matches the job>,
    "feedback": "<2-3 sentences explaining strengths and gaps>"
}}
"""

    response = model.generate_content(prompt)

    try:
        cleaned = response.text.strip().replace('```json', '').replace('```', '').strip()
        result = json.loads(cleaned)
        score = float(result.get('score', 0))
        feedback = result.get('feedback', 'No feedback generated.')
    except (json.JSONDecodeError, ValueError):
        score = 0
        feedback = "AI response could not be parsed. Please try again."

    return score, feedback