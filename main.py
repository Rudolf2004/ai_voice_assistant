from assistant.ai_engine import AIEngine

def main():
    ai = AIEngine()
    print("AI Assistant: Ready. Type your message (voice-ready architecture).")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("AI Assistant: Goodbye.")
            break

        response = ai.respond(user_input)
        print(f"AI Assistant: {response}")

if __name__ == "__main__":
    main()
