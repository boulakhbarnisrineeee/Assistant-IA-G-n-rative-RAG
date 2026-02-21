from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

DB_PATH = "faiss_index"


def build_components():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(model="llama3.1")

    return retriever, llm


def ask(query: str):
    retriever, llm = build_components()

    # Nouvelle API LangChain
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Tu es un assistant IA.
Réponds uniquement à partir du contexte suivant.

CONTEXTE :
{context}

QUESTION :
{query}
"""

    response = llm.invoke(prompt)

    sources = [doc.metadata.get("source", "unknown") for doc in docs]

    return response, sources