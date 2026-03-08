#!/usr/bin/env python3
"""
Dice Roller
Roll dice like a casino. Or like you're deciding your fate.
"""
import random
import sys

def roll_dice(num_dice=1, sides=6):
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def main():
    print("\n🎲 DICE ROLLER 🎲")
    print("=" * 40)
    
    try:
        user_input = input("Roll (e.g. 2d6, d20): ").strip().lower()
        
        if 'd' not in user_input:
            # Just a number of sides
            sides = int(user_input) if user_input else 6
            num_dice = 1
        else:
            parts = user_input.split('d')
            if parts[0] == '':
                num_dice = 1
            else:
                num_dice = int(parts[0]) if parts[0] else 1
            sides = int(parts[1]) if parts[1] else 6
        
        if num_dice < 1 or sides < 2:
            print("Invalid input!")
            return
            
        print("\nRolling...")
        
        results = roll_dice(num_dice, sides)
        
        print(f"\n🎯 Results:")
        for i, result in enumerate(results, 1):
            print(f"  Die {i}: {result}")
        
        if len(results) > 1:
            print(f"\n  Total: {sum(results)}")
        
    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\n\nCancelled.")

if __name__ == "__main__":
    main()
