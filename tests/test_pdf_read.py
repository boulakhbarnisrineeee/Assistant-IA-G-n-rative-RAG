from app.utils import extract_text_from_pdf, chunk_text
from app.embeddings import generate_embeddings
from app.database import create_collection, add_documents, query_collection


if __name__ == "__main__":
    text = extract_text_from_pdf("data/cours_ml.pdf")
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    collection = create_collection()
    add_documents(collection, chunks, embeddings)

    # Question test
    question = "Qu'est-ce qu'un algorithme génétique ?"
    question_embedding = generate_embeddings([question])[0]

    results = query_collection(collection, question_embedding, n_results=3)

    print("Résultats trouvés :")
    print(results["documents"][0])