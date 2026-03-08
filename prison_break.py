#!/usr/bin/env python3
"""
THE PRISON BREAK - Text Adventure
Navigate through Fox River like Michael Scofield.
Choose wisely. Every decision counts.
"""
import time
import sys

def print_slow(text, delay=0.03):
    """Print text like a terminal"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def chapter_1():
    print_slow("\n📺 THE PRISON BREAK - CHAPTER 1: THE PLAN\n")
    print_slow("You're Michael Scofield. You've been sent to Fox River for a crime you didn't commit.")
    print_slow("Your brother Lincoln is also here. He's scheduled for execution.")
    print_slow("You have one goal: Get both of you out.\n")
    
    print_slow("Day 1. You wake up in your cell. What's your first move?")
    print_slow("1. Talk to the cellmate - gather intel")
    print_slow("2. Explore the prison - find weaknesses")
    print_slow("3. Head to the library - research")
    
    choice = input("\n> ").strip()
    
    if choice == "1":
        chapter_2_cellmate()
    elif choice == "2":
        chapter_2_explore()
    elif choice == "3":
        chapter_2_library()
    else:
        print_slow("You stand there confused. Time passes.")
        chapter_1()

def chapter_2_cellmate():
    print_slow("\nYou approach your cellmate.")
    print_slow("'Hey, I'm Michael. You know this place well?'")
    print_slow("The cellmate looks at you. 'Name's Sucre. Yeah, I know every corner.'")
    print_slow("'But you? You're not here for long, are you?'")
    print_slow("\nYou made an ally. +1 Trust")
    print_slow(" Sucre can help you later.\n")
    chapter_3()

def chapter_2_explore():
    print_slow("\nYou walk through the prison corridors.")
    print_slow("You notice: the guards change shifts every 2 hours.")
    print_slow("There's a blind spot near the infirmary.")
    print_slow("The ventilation system looks accessible.\n")
    print_slow("You found 3 potential escape routes!")
    chapter_3()

def chapter_2_library():
    print_slow("\nYou head to the library.")
    print_slow("Books everywhere. You need blueprints. Security protocols.")
    print_slow("A guard watches you. 'You read a lot for a businessman.'")
    print_slow("You found: 'Fox River Security Systems - A Complete Guide'\n")
    print_slow("Knowledge is power. +1 Intel")
    chapter_3()

def chapter_3():
    print_slow("\n--- TO BE CONTINUED ---")
    print_slow("Michael always has a plan B. And C.")
    print_slow("Your journey has just begun...\n")

def main():
    print("\n" + "="*50)
    print("  🎬 THE PRISON BREAK - TEXT ADVENTURE 🎬")
    print("="*50)
    print("\n' 계획은 있지만, 그건 비밀입니다.'")
    print("'I have a plan. But it's a secret.'\n")
    
    start = input("Press ENTER to begin your escape... ")
    chapter_1()

if __name__ == "__main__":
    main()
