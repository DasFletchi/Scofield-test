#!/usr/bin/env python3
"""
Joke Generator
Because laughter is the best escape.
"""
import random

JOKES = {
    "tech": [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the developer go broke? Because he used up all his cache.",
        "A SQL query walks into a bar, walks up to two tables and asks... 'Can I join you?'",
        "Why do Java developers wear glasses? Because they can't C#.",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
        "A programmer's wife tells him: 'Go to the store and get a loaf of bread. If they have eggs, get a dozen.' He comes home with 12 loaves of bread.",
        "Why do programmers hate nature? It has too many bugs.",
        "The best thing about a keyboard joke is your fingers can rest.",
    ],
    "office": [
        "I told my boss I needed a raise because three companies were after me. He asked which ones. I said Gas, Electric, and Water.",
        "My boss told me to have a good day.. so I went home.",
        "I used to work at a calendar factory, but I got fired for taking a couple of days off.",
        "My grandfather has the heart of a lion and a lifetime ban from the zoo.",
        "I'm not lazy, I'm just on energy-saving mode.",
    ],
    "random": [
        "Why did the chicken cross the road? To prove to the possum it could be done.",
        "I'm not saying I'm Batman. I'm just saying no one has ever seen me and Batman in a room together.",
        "I have a lot of growing up to do. I realized that the other day inside my fort.",
        "My bed is a magical place where I suddenly remember everything I forgot to do.",
        "I'm not arguing, I'm just explaining why I'm right.",
    ]
}

def main():
    print("\n😂 JOKE GENERATOR 😂")
    print("=" * 40)
    print("Categories: tech, office, random")
    
    category = input("Category (or random): ").strip().lower()
    
    if category not in JOKES:
        # Random category
        all_jokes = []
        for jokes in JOKES.values():
            all_jokes.extend(jokes)
        joke = random.choice(all_jokes)
    else:
        joke = random.choice(JOKES[category])
    
    print(f"\n{joke}\n")

if __name__ == "__main__":
    main()
