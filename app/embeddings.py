from sentence_transformers import SentenceTransformer


# Charger le modèle une seule fois
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    """
    Génère les embeddings pour une liste de textes (chunks).
    """
    embeddings = model.encode(texts)
    return embeddings