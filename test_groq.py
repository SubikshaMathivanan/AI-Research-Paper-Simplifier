from services.groq_provider import generate

response = generate(
    "Explain machine learning in one sentence."
)

print(response)