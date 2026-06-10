from services.llm_service import ask_llm

def chat_with_paper(paper_text, question):

    prompt = f"""
    You are an AI assistant.

    Answer the user's question ONLY using the research paper.

    Research Paper:
    {paper_text[:5000]}

    Question:
    {question}
    """

    return ask_llm(prompt)