from app.rag import ask

print("🤖 Assistant IA Générative (RAG)")
print("Tape 'exit' pour quitter.\n")

while True:
    question = input("❓ Votre question : ")

    if question.lower() in ["exit", "quit"]:
        print("👋 Au revoir !")
        break

    ask(question)
    print("\n" + "-" * 50 + "\n")
    