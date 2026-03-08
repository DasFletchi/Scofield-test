#!/usr/bin/env python3
"""
Alarm Clock
Set an alarm. Don't be late.
"""
import time
import os
import sys

def set_alarm(hour, minute):
    print(f"\n⏰ Alarm set for {hour:02d}:{minute:02d}")
    print("Press Ctrl+C to cancel\n")
    
    while True:
        now = time.localtime()
        current_hour = now.tm_hour
        current_minute = now.tm_min
        
        if current_hour == hour and current_minute == minute:
            print("\n" + "="*40)
            print("🔔 WAKE UP! 🔔")
            print("="*40)
            # Play a sound (beep)
            for _ in range(5):
                sys.stdout.write("\a")
                sys.stdout.flush()
                time.sleep(0.5)
            break
        
        # Display time every minute
        timer = f"{current_hour:02d}:{current_minute:02d}"
        print(f"\rWaiting... {timer}", end="", flush=True)
        time.sleep(30)  # Check every 30 seconds

def main():
    print("\n⏰ ALARM CLOCK ⏰")
    print("=" * 40)
    
    try:
        time_str = input("Time (HH:MM, 24h): ").strip()
        hour, minute = map(int, time_str.split(':'))
        
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            print("Invalid time!")
            return
            
        set_alarm(hour, minute)
        
    except ValueError:
        print("Please enter time in HH:MM format!")
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled.")

if __name__ == "__main__":
    main()
