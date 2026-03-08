#!/usr/bin/env python3
"""
ASCII Art Generator
Because sometimes you need to make a statement.
"""
import random

ARTWORKS = {
    "scofield": r"""
    ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
    ⭐  _____ _   _  _____ ⭐
    ⭐ |_   _|| \ | ||  ___| ⭐
    ⭐   | |  |  \| || |__  ⭐
    ⭐   | |  | . ` ||  __| ⭐
    ⭐   | |  | |\  || |___ ⭐
    ⭐   \_/  \_| \_/\____/ ⭐
    ⭐                     ⭐
    ⭐  "I have a plan."    ⭐
    ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
    """,
    "robot": r"""
        ┌─────────────────────┐
        │   🤖 BOOTING...   │
        └─────────────────────┘
              ╔═══╗
              ║ ◉ ║
              ╚═══╝
             ╔═════╗
            ╔╝     ╚╗
            ║ ◉   ◉ ║
            ╚╗     ╔╝
             ╚═════╝
        ┌─────────────────────┐
        │   SYSTEMS ONLINE   │
        └─────────────────────┘
    """,
    "prison": r"""
    ┌────────────────────────────┐
    │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │ ██
    │ ▓                        ▓ │ ██
    │ ▓   PRISON BREAK         ▓ │ ██
    │ ▓                        ▓ │ ██
    │ ▓   Plan: ACTIVE         ▓ │ ██
    │ ▓                        ▓ │ ██
    │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │ ██
    └────────────────────────────┘
    """,
    "fire": r"""
           _=_
         (ogle )
        / /| |\ 
       (_(  |_/
         \  /
          ))
         // 
        ((
    """,
    "rocket": r"""
              🚀
             ///
            (o o)
           (  V  )
          --m-m--
    """,
    "random": [
        r"""
   /\_/\  
  ( o.o ) 
   > ^ <
        """,
        r"""
    _____
   /     \
   | () |
   |     |
   \_____/
        """,
        r"""
   🎮
  ┌───┐
  │ ▲ │
  └───┘
        """,
    ]
}

def main():
    print("\n🎨 ASCII ART GENERATOR 🎨")
    print("=" * 40)
    
    print("\nAvailable art:")
    for key in ARTWORKS:
        if key != "random":
            print(f"  - {key}")
    print("  - random")
    
    choice = input("\nChoice: ").strip().lower()
    
    if choice == "random":
        art = random.choice(ARTWORKS["random"])
    elif choice in ARTWORKS:
        art = ARTWORKS[choice]
    else:
        print("Not found!")
        return
    
    print("\n" + "="*40)
    print(art)
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
