import streamlit as st
from app.rag import ask

# ------------------ Configuration de la page ------------------
st.set_page_config(
    page_title="Assistant IA RAG",
    page_icon="🤖",
    layout="wide"
)

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("⚙️ Paramètres")
    st.write("Assistant IA basé sur des documents PDF")
    st.markdown("---")

    if st.button("🗑️ Effacer l’historique"):
        st.session_state.messages = []

# ------------------ Initialisation de l’historique ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ Titre ------------------
st.markdown(
    """
    <h1 style="text-align: center;">🤖 Assistant IA Générative (RAG)</h1>
    <p style="text-align: center; color: gray;">
    Pose des questions basées uniquement sur les documents PDF.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ------------------ Affichage de l’historique (chat) ------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑‍💻 Toi :** {msg['content']}")
    else:
        st.markdown(
            """
            <div style="
                background-color:#1e1e1e;
                padding:15px;
                border-radius:10px;
                border-left:4px solid #4CAF50;
                margin-bottom:10px;
            ">
            <<b>🤖 Assistant :</b>
            </div>
            """,
            unsafe_allow_html=True
        )



st.write(msg["content"])
# ------------------ Zone de saisie ------------------
question = st.text_input(
    "❓ Ta question",
    placeholder="Ex : Explique le CSP"
)

if st.button("🔍 Envoyer"):
    if question.strip():
        # Ajouter la question
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.spinner("⏳ Recherche de la réponse..."):
            response, sources = ask(question)

        # Construire la réponse finale
        answer_text = response + "\n\n📌 Sources :\n"
        for src in set(sources):
            answer_text += f"- {src}\n"

        # Ajouter la réponse
        st.session_state.messages.append(
            {"role": "assistant", "content": answer_text}
        )

    else:
        st.warning("⚠️ Merci de saisir une question.")