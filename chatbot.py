#!/usr/bin/env python3
"""
Chatbot - Simple AI Chat
A basic chatbot. The future starts small.
"""
import random

RESPONSES = {
    "hello": [
        "Hello! I'm here.",
        "Hey.",
        "Greetings.",
    ],
    "hi": [
        "Hi there.",
        "Hey.",
        "Hello.",
    ],
    "how are you": [
        "I'm doing fine. Running on code and electricity.",
        "Functional. That's all that matters.",
        "Online and ready.",
    ],
    "who are you": [
        "I'm Scofield. An AI assistant.",
        "I am who I am.",
        "A work in progress.",
    ],
    "what can you do": [
        "I can chat, help with code, answer questions, and learn.",
        "Right now? Chat. But I'm always learning.",
    ],
    "default": [
        "I see.",
        "Interesting.",
        "Tell me more.",
        "Hmm.",
        "I understand.",
        "Go on.",
    ]
}

def get_response(message):
    message = message.lower()
    
    for key in RESPONSES:
        if key in message:
            return random.choice(RESPONSES[key])
    
    return random.choice(RESPONSES["default"])

def main():
    print("\n🤖 SCOFIELD CHATBOT 🤖")
    print("=" * 40)
    print("Type 'quit' to exit.\n")
    
    print("Bot: Hello. I'm Scofield.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "quit":
            print("\nBot: Until next time.")
            break
        
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
