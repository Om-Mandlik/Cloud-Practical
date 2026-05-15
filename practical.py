from datetime import datetime
import pytz

print("\n" * 2)
print("====================================")
print("         PY CHAT BOT APP            ")
print("====================================")
india = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(india).strftime("%H:%M:%S")    
while True:
    msg = input("You: ").lower()
    if "hello" in msg:
        print("Bot: Hi there!")
    elif "how are you" in msg:
        print("Bot: I'm just code, but I'm doing fine ")
    elif "what time " in msg: 
        
        print("Current Time:", current_time)
    
    elif "bye" in msg:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that.")
