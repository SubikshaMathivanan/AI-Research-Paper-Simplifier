from services.groq_provider import generate

def ask_llm(prompt):

    try:
        return generate(prompt)

    except Exception as e:
        return f"ERROR: {str(e)}"