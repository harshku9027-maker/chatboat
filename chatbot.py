import random

# Responses
responses = {
    "hello": ["Hi!", "Hello!"],
    "bye": ["Goodbye!", "See you!"],
    "thanks": ["You're welcome!", "No problem!"],
    "how are you": ["I'm good, thanks!", "Doing great!"],
}

# Main loop
print("ChatBot: Hi! Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()
    
    if "bye" in user:
        print("ChatBot: Goodbye!")
        break
    elif "hello" in user or "hi" in user:
        print("ChatBot:", random.choice(responses["hello"]))
    elif "thanks" in user or "thank you" in user:
        print("ChatBot:", random.choice(responses["thanks"]))
    elif "how are you" in user:
        print("ChatBot:", random.choice(responses["how are you"]))
    else:
        print("ChatBot: I don't understand. Try again!")
        