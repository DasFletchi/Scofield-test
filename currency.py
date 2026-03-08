#!/usr/bin/env python3
"""
Currency Converter
Because even escape artists need to know exchange rates.
"""
import json
import time

# Static rates (would need API for real-time)
RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "CHF": 0.88,
    "CAD": 1.36,
    "AUD": 1.53,
    "INR": 83.12,
}

def convert(amount, from_curr, to_curr):
    if from_curr not in RATES or to_curr not in RATES:
        return None
    
    # Convert to USD first, then to target
    usd_amount = amount / RATES[from_curr]
    result = usd_amount * RATES[to_curr]
    return result

def main():
    print("\n💱 CURRENCY CONVERTER 💱")
    print("=" * 40)
    print("Available currencies:")
    for code in sorted(RATES.keys()):
        print(f"  {code}", end=" ")
    print("\n")
    
    try:
        amount = float(input("Amount: "))
        from_curr = input("From (e.g. USD): ").upper()
        to_curr = input("To (e.g. EUR): ").upper()
        
        result = convert(amount, from_curr, to_curr)
        
        if result is None:
            print("Invalid currency code!")
            return
            
        print(f"\nConverting...")
        time.sleep(0.5)
        print(f"\n💰 {amount} {from_curr} = {result:.2f} {to_curr}")
        
    except ValueError:
        print("Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\nCancelled.")

if __name__ == "__main__":
    main()
