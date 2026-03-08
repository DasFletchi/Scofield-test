#!/usr/bin/env python3
"""
Countdown Timer
Because sometimes you need to know how much time is left.
"""
import time
import sys

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏰ {timer}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    
    print("\r\n⏰ 00:00")
    print("🔔 TIME'S UP!")

def main():
    print("\n⏱️ COUNTDOWN TIMER ⏱️")
    print("=" * 40)
    print("Enter time in seconds or MM:SS format")
    
    try:
        user_input = input("Time: ").strip()
        
        if ':' in user_input:
            mins, secs = user_input.split(':')
            total = int(mins) * 60 + int(secs)
        else:
            total = int(user_input)
        
        if total <= 0:
            print("Please enter a positive number!")
            return
            
        print(f"\nStarting countdown from {total} seconds...")
        time.sleep(1)
        countdown(total)
        
    except ValueError:
        print("Invalid input!")
    except KeyboardInterrupt:
        print("\n\nTimer cancelled.")

if __name__ == "__main__":
    main()
