#!/usr/bin/env python3
"""
Stopwatch
Time yourself. Every second counts.
"""
import time
import sys
import signal

running = False
start_time = 0

def signal_handler(sig, frame):
    global running
    if running:
        running = False
        elapsed = time.time() - start_time
        print(f"\n\n⏱️ Final Time: {elapsed:.2f} seconds")
        sys.exit(0)

def main():
    global running, start_time
    
    print("\n⏱️ STOPWATCH ⏱️")
    print("=" * 40)
    print("Press ENTER to start...")
    input()
    
    start_time = time.time()
    running = True
    
    print("\nRunning... Press Ctrl+C to stop")
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        while running:
            elapsed = time.time() - start_time
            mins, secs = divmod(int(elapsed), 60)
            print(f"\r⏰ {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False
        print(f"\n\n⏱️ Time: {elapsed:.2f}s")

if __name__ == "__main__":
    main()
