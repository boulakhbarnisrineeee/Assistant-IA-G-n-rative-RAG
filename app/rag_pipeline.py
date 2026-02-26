import ollama


def build_prompt(context, question):
    prompt = f"""
Tu es un assistant utile.

Réponds UNIQUEMENT en utilisant les informations présentes dans le contexte.
Ne rajoute aucune information extérieure.
Ne pose pas de question supplémentaire.
Ne fais pas d'extrapolation.


Si la réponse n'est pas présente dans le contexte, dis :
"Je ne trouve pas l'information dans le document."

Contexte :
{context}

Question :
{question}

Réponse :
"""
    return prompt


def generate_answer(context_chunks, question):
    context = "\n\n".join(context_chunks)
    prompt = build_prompt(context, question)

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response["message"]["content"]