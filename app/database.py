import chromadb
from chromadb.config import Settings


# Créer un client local
client = chromadb.Client(Settings(persist_directory="./chroma_db"))


def create_collection(collection_name="rag_collection"):
    """
    Crée ou récupère une collection ChromaDB.
    """
    collection = client.get_or_create_collection(name=collection_name)
    return collection


def add_documents(collection, chunks, embeddings, source_name="uploaded_document"):
    ids = [str(i) for i in range(len(chunks))]
    metadatas = [{"source": source_name, "chunk_id": i} for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids,
        metadatas=metadatas
    )


def query_collection(collection, query_embedding, n_results=3):
    """
    Recherche les chunks les plus proches d'une question.
    """
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )
    return results