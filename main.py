from file_agent import process_user_query

if __name__ == "__main__":
    print("📁 File ChatBot is ready! Ask me about your local files.")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Bot: Goodbye!")
                break
            response = process_user_query(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            print("\nBot: Bye!")
            break

