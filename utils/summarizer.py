from services.llm_service import ask_llm

def generate_summary(text):

    prompt = f"""
    Summarize this research paper in simple language.

    Paper:

    {text[:5000]}
    """

    return ask_llm(prompt)