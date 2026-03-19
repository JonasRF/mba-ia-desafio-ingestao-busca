from search import search_prompt

def main():
    
    print("-" * 50)
    print("Sistema de ingestão e busca semântica com LangChain e PostGres")
    print("Digite 'quit', 'exit', 'sair' ou 'q' para encerrar a sessão")
    print("-" * 50)
    print("\n🤖 Chat iniciado!\n")

    while True:
        try:
            # variável principal
            question = input("Faça sua pergunta: ")

            if question.lower() in ["sair", "exit", "quit", "q"]:
                print("\nEncerrando chat... Até logo! 👋")
                break

            print("🔎 Iniciando busca...\n")

            response = search_prompt(question=question)

            if not response:
                print("⚠️ Não foi possível obter resposta.\n")
                continue

            # 👇 EXIBE A RESPOSTA
            print(f"🤖 Resposta:\n{response.content}\n")

        except KeyboardInterrupt:
            print("\nSessão de chat interrompida. Até logo!")
            break

if __name__ == "__main__":
    main()