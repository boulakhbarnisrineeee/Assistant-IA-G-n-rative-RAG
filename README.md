# 🤖 Assistant IA Générative basé sur RAG (Retrieval-Augmented Generation)

## 📌 Description
Ce projet implémente un **assistant IA génératif** capable de répondre à des questions **en s’appuyant exclusivement sur un ensemble de documents PDF**.  
Il repose sur une architecture **RAG (Retrieval-Augmented Generation)** combinant recherche sémantique et génération de texte via un **LLM local**.

L’application propose une **interface web interactive** de type chat, permettant de consulter les réponses générées ainsi que les **sources PDF utilisées**.

---

## 🎯 Objectifs
- Exploiter des documents PDF comme **source de connaissance fiable**
- Réduire les hallucinations en contraignant le modèle au **contexte récupéré**
- Mettre en pratique les concepts clés de **NLP et IA générative**
- Proposer une **interface utilisateur simple et intuitive**

---

## 🧠 Architecture RAG
Le pipeline suit les étapes suivantes :

1. **Ingestion des documents**
   - Chargement des fichiers PDF
   - Découpage en segments (chunks)
   - Génération d’embeddings

2. **Indexation vectorielle**
   - Stockage des embeddings dans une base **FAISS**

3. **Recherche sémantique**
   - Récupération des passages les plus pertinents par similarité vectorielle

4. **Génération de réponse**
   - Construction d’un prompt enrichi par le contexte
   - Génération de la réponse avec un **LLM local (Ollama – Llama 3.1)**

5. **Affichage**
   - Réponse générée
   - Sources PDF associées

---

## 🖥️ Interface utilisateur
L’interface web (Streamlit) permet :
- de poser des questions en langage naturel,
- d’afficher les réponses générées,
- de consulter les **sources PDF**,
- de conserver un **historique de conversation (chat)**,
- d’effacer l’historique à tout moment.

---

## 📁 Structure du projet
RAG_Assistant/
│
├── app/
│   ├── __init__.py
│   ├── ingest.py        # Ingestion et indexation des PDF
│   ├── rag.py           # Logique RAG (retrieval + génération)
│   └── cli.py           # Interface en ligne de commande (optionnelle)
│
├── data/
│   ├── 7_csp_modeling_chap8.pdf
│   ├── 8_game_theory_intro.pdf
│   └── 9_adversarial_search.pdf
│
├── faiss_index/         # Index vectoriel FAISS
├── streamlit_app.py     # Interface web Streamlit
├── venv/                # Environnement virtuel
└── README.md


---

## ⚙️ Technologies utilisées
- **Python**
- **LangChain**
- **FAISS**
- **HuggingFace Embeddings** (`all-MiniLM-L6-v2`)
- **Ollama** (LLM local – Llama 3.1)
- **Streamlit**

---

## ▶️ Installation et exécution

### 1️⃣ Cloner le projet
```bash
git clone <repo-url>
cd RAG_Assistant


### 2️⃣ Créer et activer l’environnement virtuel
python -m venv venv
venv\Scripts\activate   # Windows


3️⃣ Installer les dépendances
pip install streamlit langchain langchain-community faiss-cpu sentence-transformers ollama


4️⃣ Ingestion des documents
python app/ingest.py


5️⃣ Lancer l’application web
streamlit run streamlit_app.py



✅ Fonctionnalités

✔️ Recherche sémantique sur documents PDF

✔️ Génération de réponses contextualisées

✔️ Affichage des sources utilisées

✔️ Interface web interactive

✔️ Historique de conversation

✔️ LLM local (sans API externe)
