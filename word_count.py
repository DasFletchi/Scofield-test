#!/usr/bin/env python3
"""
Word Counter
Count words, characters, lines in text.
"""
import os

def count_text(text):
    lines = text.split('\n')
    words = text.split()
    characters = len(text)
    characters_no_spaces = len(text.replace(' ', ''))
    
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
        "characters_no_spaces": characters_no_spaces
    }

def main():
    print("\n📝 WORD COUNTER 📝")
    print("=" * 40)
    
    print("1. Enter text")
    print("2. Count from file")
    
    try:
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            print("\nEnter text (Ctrl+D or Ctrl+Z to finish):")
            text = sys.stdin.read()
            counts = count_text(text)
            
            print("\n📊 Results:")
            print(f"  Lines: {counts['lines']}")
            print(f"  Words: {counts['words']}")
            print(f"  Characters: {counts['characters']}")
            print(f"  Characters (no spaces): {counts['characters_no_spaces']}")
            
        elif choice == "2":
            filename = input("Filename: ").strip()
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    text = f.read()
                counts = count_text(text)
                
                print(f"\n📊 Results for {filename}:")
                print(f"  Lines: {counts['lines']}")
                print(f"  Words: {counts['words']}")
                print(f"  Characters: {counts['characters']}")
            else:
                print("File not found!")
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    main()
