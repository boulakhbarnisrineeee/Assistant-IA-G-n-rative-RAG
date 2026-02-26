# 📚 RAG Academic Assistant

Ce projet est un projet personnel d’apprentissage autour de la **Retrieval-Augmented Generation (RAG)**.
Il permet de poser des questions à un document PDF et d’obtenir des réponses basées uniquement sur le contenu de ce document.

- 🐍 Python  
- 🧠 SentenceTransformers (Embeddings)  
- 🗄 ChromaDB (Vector Database)  
- 🤖 Mistral (via Ollama - local LLM)  
- 🎨 Streamlit 

---
## 🛠 Outils et technologies utilisés

Les outils utilisés dans ce projet sont volontairement simples :

-Python : Langage principal du projet.

-SentenceTransformers : Modèle de génération des embeddings  **all-MiniLM-L6-v2**

-ChromaDB : base de données vectorielle ( Stockage des embeddings) + Recherce sémantique(Top-K retrieval)

-OLLama : Runtime Local executer le modele Msitral

-Mistral (via Ollama) : LLM open-source executé en local qui genere les reponses (pas d'API externe)

-Streamlit : Interface utilisateur

- PyMuPDF (fitz) : extraction du texte depuis des documents PDF

- Numpy : calcul de similarite cosinus entre les vecteurs + evaluation semantique 

---

## 🎯 Objectif du projet

-Comprendre comment interroger un document PDF avec une approche sémantique
-Découvrir le principe des embeddings
-Mettre en place une base vectorielle
-Générer des réponses à partir d’un contexte récupéré, et non de connaissances externes
---Si l’information demandée n’existe pas dans le document, le système l’indique clairement.


---

## 🧠 How It Works

1. 📄 Un document PDF est chargé et son texte est extrait depuis le PDF
2. ✂️ Le texte est découpé en petits segments (chunks) 
3. 🔢 Chaque segment est transformé en vecteur (embedding) 
4. 🗄 Les embeddings sont stockés dans une base vectorielle ''ChromaDB''
5. ❓ La question de l’utilisateur est vectorisée
6. 🔍 Les passages les plus proches sont récupérés 
7. 🤖 Mistral genere une réponse est générée à partir de ces passages

---

## 🏗 Structure de projet 

rag-academic-assistant/
│
├── app/
│   ├── utils.py           # Extraction du texte et découpage en chunks
│   ├── embeddings.py      # Génération des embeddings
│   ├── database.py        # Gestion de la base vectorielle
│   ├── rag_pipeline.py    # Logique RAG et génération de réponses
│   └── main.py            # interface utilisateur
│
├── tests/
│   ├── test_install.py    # Vérification de l’environnement
│   ├── test_pdf_read.py   # Test du pipeline RAG
│   └── evaluation.py      # Évaluation simple des réponses
│
├── data/
│   └── documents/         # Documents PDF utilisés pour les tests
│
├── requirements.txt
└── README.md

---

## 🔎 Tests et évaluation 
Dans le dossier **tests** :
-Vérifier que l’environnement est bien installé
-Tester la lecture et l’analyse d’un PDF
-Évaluer la qualité des réponses selon le nombre de chunks récupérés




