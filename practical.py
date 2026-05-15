while True:
    print("\n" * 2)
    print("====================================")
    print("        🤖 PY CHAT BOT APP        ")
    print("====================================")
    msg = input("You: ").lower()

    if "hello" in msg:
        print("Bot: Hi there!")
    elif "how are you" in msg:
        print("Bot: I'm just code, but I'm doing fine 😄")
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that.")
