import streamlit as st
import numpy as np

from app.utils import extract_text_from_pdf, chunk_text
from app.embeddings import generate_embeddings
from app.database import create_collection, add_documents, query_collection
from app.rag_pipeline import generate_answer


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="RAG Academic Assistant", layout="wide")

st.title("📚 RAG Academic Assistant")
st.write("Pose une question sur le document PDF téléchargé.")


# -------------------------------------------------
# Cosine Similarity
# -------------------------------------------------
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


# -------------------------------------------------
# Upload PDF
# -------------------------------------------------
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:

    temp_path = "temp_uploaded.pdf"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    # -------------------------------------------------
    # Process Document (Only Once)
    # -------------------------------------------------
    if "collection_created" not in st.session_state:

        with st.spinner("Processing and indexing document..."):

            text = extract_text_from_pdf(temp_path)
            chunks = chunk_text(text)
            embeddings = generate_embeddings(chunks)

            collection = create_collection()
            add_documents(
                collection,
                chunks,
                embeddings,
                source_name=uploaded_file.name
            )

            st.session_state.collection = collection
            st.session_state.collection_created = True

        st.success("📌 Document processed and indexed successfully!")

    # -------------------------------------------------
    # Question Section
    # -------------------------------------------------
    st.divider()

    question = st.text_input("💬 Ask a question about the document")
    top_k = st.slider("🔎 Number of retrieved chunks (Top-K)", 1, 5, 3)

    if question:

        with st.spinner("Generating answer..."):

            question_embedding = generate_embeddings([question])[0]

            results = query_collection(
                st.session_state.collection,
                question_embedding,
                n_results=top_k
            )

            context_chunks = results["documents"][0]
            metadatas = results["metadatas"][0]

            answer = generate_answer(context_chunks, question)

            # Compute semantic similarity
            context_text = " ".join(context_chunks)
            context_embedding = generate_embeddings([context_text])[0]
            answer_embedding = generate_embeddings([answer])[0]

            similarity = cosine_similarity(context_embedding, answer_embedding)

        # -------------------------------------------------
        # Display Answer
        # -------------------------------------------------
        st.subheader("🧠 Answer")
        st.write(answer)

        st.metric("🔬 Semantic Similarity (Answer ↔ Context)", f"{similarity:.4f}")

        # -------------------------------------------------
        # Conditional Sources Display
        # -------------------------------------------------
        if "Je ne trouve pas l'information" in answer:
            st.warning("⚠️ No relevant information found in the document.")
        else:
            st.subheader("📖 Sources")

            unique_sources = {}

            for chunk, metadata in zip(context_chunks, metadatas):
                source = metadata["source"]
                chunk_id = metadata["chunk_id"]

                if source not in unique_sources:
                    unique_sources[source] = []

                unique_sources[source].append((chunk_id, chunk))

            for source, chunks in unique_sources.items():
                st.markdown(f"### 📌 Source: {source}")

                for chunk_id, chunk in chunks:
                    st.markdown(f"**Chunk ID:** {chunk_id}")
                    st.code(chunk[:500])