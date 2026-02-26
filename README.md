# 📚 RAG Academic Assistant

This project implements a **Retrieval-Augmented Generation (RAG)** system for document-based question answering using:

- 🐍 Python  
- 🧠 SentenceTransformers (Embeddings)  
- 🗄 ChromaDB (Vector Database)  
- 🤖 Mistral (via Ollama - local LLM)  
- 🎨 Streamlit (UI - upcoming)

---

## 🎯 Project Objective

The goal of this project is to build a system capable of answering user questions based strictly on uploaded PDF documents.

The model does not rely on external knowledge but only on retrieved document context.

---

## 🧠 How It Works

1. 📄 PDF is loaded and text is extracted  
2. ✂️ Text is split into overlapping chunks  
3. 🔢 Each chunk is converted into embeddings  
4. 🗄 Embeddings are stored in ChromaDB  
5. ❓ A user question is embedded  
6. 🔍 Most relevant chunks are retrieved  
7. 🤖 Mistral generates a response using retrieved context  

---

## 🏗 Project Structure

 rag-academic-assistant/
│
├── data/documents/ # PDF files
├── app/
│ ├── utils.py # PDF extraction & chunking
│ ├── embeddings.py # Embedding generation
│ ├── database.py # ChromaDB integration
│ ├── rag_pipeline.py # Prompt + LLM interaction
│
├── tests/
│ └── test_pdf_read.py
│
├── requirements.txt
└── README.md


---

## 🚀 Running the Project

### 1️⃣ Install dependencies & Pull Mistral model (only once) & Run test pipeline

```bash
pip install -r requirements.txt
ollama pull mistral
python -m tests.test_pdf_read


---

## 🔎 Evaluation 
The system supports testing different retrieval sizes (Top-3 vs Top-5 chunks) to evaluate response quality and context relevance.

---

## 🧩 Key Concepts Implemented

Semantic Search

Vector Databases

Embedding Models

Prompt Engineering

Retrieval-Augmented Generation

Local LLM Deployment



---

## 📌 Future Improvements

Streamlit interface

Source citation display

Multi-document support

Reranking mechanism

Chunk size optimization