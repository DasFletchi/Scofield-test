#!/usr/bin/env python3
"""
Flashcard Study
Learn with spaced repetition. The smart way.
"""
import random
import os
import json

DECK_FILE = "deck.json"

def load_deck():
    if os.path.exists(DECK_FILE):
        with open(DECK_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_deck(deck):
    with open(DECK_FILE, 'w') as f:
        json.dump(deck, f, indent=2)

def add_card(deck):
    front = input("Front (question): ").strip()
    back = input("Back (answer): ").strip()
    deck[front] = back
    print(f"✓ Added: {front}")

def study(deck):
    if not deck:
        print("No cards to study!")
        return
    
    cards = list(deck.items())
    random.shuffle(cards)
    
    correct = 0
    total = len(cards)
    
    print(f"\n📚 Studying {total} cards...")
    print("Press Enter to reveal answer. Type 'q' to quit.\n")
    
    for front, back in cards:
        print(f"Q: {front}")
        input("Press Enter for answer...")
        print(f"A: {back}")
        
        result = input("\n[K]nown? [W]rong? (k/w/q): ").lower()
        
        if result == 'k':
            correct += 1
        elif result == 'q':
            break
    
    print(f"\n📊 Score: {correct}/{total} ({100*correct//total if total > 0 else 0}%)")

def list_cards(deck):
    if not deck:
        print("No cards!")
        return
    print("\n📋 Your Cards:")
    for i, (front, back) in enumerate(deck.items(), 1):
        print(f"{i}. Q: {front}")
        print(f"   A: {back}\n")

def main():
    print("\n📚 FLASHCARD STUDY 📚")
    print("=" * 40)
    
    deck = load_deck()
    
    print("Commands: add, study, list, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "quit" or cmd == "q":
            break
        elif cmd == "add" or cmd == "a":
            add_card(deck)
            save_deck(deck)
        elif cmd == "study" or cmd == "s":
            study(deck)
        elif cmd == "list" or cmd == "l":
            list_cards(deck)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
