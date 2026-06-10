from services.llm_service import ask_llm

def difficulty_analysis(text):

    prompt = f"""
    Analyze this research paper.

    Give:
    1. Difficulty score out of 10
    2. Why it received that score
    3. Prerequisites needed

    Paper:

    {text[:5000]}
    """

    return ask_llm(prompt)