import time
import numpy as np

from app.utils import extract_text_from_pdf, chunk_text
from app.embeddings import generate_embeddings
from app.database import create_collection, add_documents, query_collection
from app.rag_pipeline import generate_answer


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def evaluate_k_values(pdf_path, question, k_values=[1, 3, 5]):

    print("🔍 Processing document...\n")

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    collection = create_collection("evaluation_collection")
    add_documents(collection, chunks, embeddings)

    question_embedding = generate_embeddings([question])[0]

    for k in k_values:

        print("=" * 70)
        print(f"📊 Testing Top-{k} Retrieval\n")

        # -----------------------------
        # Retrieval Timing
        # -----------------------------
        start_retrieval = time.time()

        results = query_collection(
            collection,
            question_embedding,
            n_results=k
        )

        retrieval_time = time.time() - start_retrieval

        context_chunks = results["documents"][0]
        context_text = " ".join(context_chunks)

        # -----------------------------
        # Generation Timing
        # -----------------------------
        start_generation = time.time()

        answer = generate_answer(context_chunks, question)

        generation_time = time.time() - start_generation

        # -----------------------------
        # Similarity Score
        # -----------------------------
        context_embedding = generate_embeddings([context_text])[0]
        answer_embedding = generate_embeddings([answer])[0]

        similarity = cosine_similarity(context_embedding, answer_embedding)

        # -----------------------------
        # Results
        # -----------------------------
        print("🧠 Generated Answer:\n")
        print(answer)
        print("\n")

        print(f"📏 Answer length: {len(answer)} characters")
        print(f"⏱ Retrieval time: {retrieval_time:.3f} sec")
        print(f"⏱ Generation time: {generation_time:.3f} sec")
        print(f"🔎 Semantic similarity (Answer ↔ Context): {similarity:.4f}")
        print("\n")


if __name__ == "__main__":

    pdf_path = "data/cours_ml.pdf"
    question = "Qu'est-ce qu'un algorithme génétique ?"

    evaluate_k_values(pdf_path, question, k_values=[1, 3, 5])