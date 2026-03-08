#!/usr/bin/env python3
"""
Rock Paper Scissors - But make it Spy
Because sometimes you need to make decisions under pressure.
"""
import random
import time
import sys

CHOICES = {
    '1': ('🪨', 'Rock'),
    '2': ('📄', 'Paper'), 
    '3': ('✂️', 'Scissors')
}

def get_computer_choice():
    return random.choice(['1', '2', '3'])

def determine_winner(player, computer):
    # Rock (1) beats Scissors (3)
    # Scissors (3) beats Paper (2)
    # Paper (2) beats Rock (1)
    if player == computer:
        return 'tie'
    if (player == '1' and computer == '3') or \
       (player == '3' and computer == '2') or \
       (player == '2' and computer == '1'):
        return 'win'
    return 'lose'

def main():
    print("\n🎮 ROCK PAPER SCISSORS - SPY EDITION 🎮")
    print("=" * 45)
    print("In the field, every choice matters.")
    print("Choose wisely.\n")
    
    score = {'win': 0, 'lose': 0, 'tie': 0}
    
    while True:
        print("\nMake your move:")
        print("  [1] 🪨 Rock")
        print("  [2] 📄 Paper")
        print("  [3] ✂️ Scissors")
        print("  [Q] Quit")
        
        player = input("\n> ").strip().lower()
        
        if player == 'q':
            print("\n--- FINAL SCORE ---")
            print(f"  Wins:    {score['win']}")
            print(f"  Losses:  {score['lose']}")
            print(f"  Ties:    {score['tie']}")
            print("\nEvery mission ends. This one is complete.")
            break
        
        if player not in ['1', '2', '3']:
            print("Invalid choice, agent. Try again.")
            continue
        
        computer = get_computer_choice()
        
        print("\nDeciding...")
        time.sleep(0.8)
        
        print(f"\nYou:      {CHOICES[player][0]} {CHOICES[player][1]}")
        print(f"Enemy:    {CHOICES[computer][0]} {CHOICES[computer][1]}")
        
        result = determine_winner(player, computer)
        
        if result == 'win':
            print("\n✅ You win this round!")
            score['win'] += 1
        elif result == 'lose':
            print("\n❌ They win this time.")
            score['lose'] += 1
        else:
            print("\n⚖️ Stalemate.")
            score['tie'] += 1

if __name__ == "__main__":
    main()
