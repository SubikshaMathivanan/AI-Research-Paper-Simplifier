from services.llm_service import ask_llm

def explain_for_beginner(text):

    prompt = f"""
    Explain this research paper to a beginner student.

    Use simple language.

    Paper:

    {text[:5000]}
    """

    return ask_llm(prompt)