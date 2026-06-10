from services.llm_service import ask_llm
import re

def generate_viva_questions(text):

    prompt = f"""
Generate 10 viva questions from this research paper.

Rules:
- Each question must be complete and meaningful
- Number them 1 to 10
- One question per line only
- No explanations

Paper:
{text[:5000]}
"""

    response = ask_llm(prompt)

    # 🧹 FIX: remove weird character splitting issues
    response = response.replace("\n", " ").strip()

    # split using numbers (1., 2., etc.)
    questions = re.split(r"\d+\.", response)

    # clean list
    questions = [q.strip() for q in questions if q.strip()]

    return questions