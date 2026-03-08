#!/usr/bin/env python3
"""
Binary Converter
Convert between text, binary, hex, and decimal.
Because Michael Scofield would appreciate the elegance of numbers.
"""
import sys

def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    try:
        binaries = binary.split()
        return ''.join(chr(int(b, 2)) for b in binaries)
    except:
        return "Invalid binary!"

def text_to_hex(text):
    return ' '.join(hex(ord(c))[2:].upper() for c in text)

def hex_to_text(hex_str):
    try:
        hexes = hex_str.split()
        return ''.join(chr(int(h, 16)) for h in hexes)
    except:
        return "Invalid hex!"

def decimal_to_text(dec_str):
    try:
        decimals = dec_str.split()
        return ''.join(chr(int(d)) for d in decimals)
    except:
        return "Invalid decimal!"

def main():
    print("\n🔢 BINARY CONVERTER 🔢")
    print("=" * 40)
    print("Convert: text <-> binary, hex, decimal")
    print("Examples:")
    print("  text -> binary: 'Hi' -> '01001000 01101001'")
    print("  text -> hex:    'Hi' -> '48 69'")
    print("  text -> dec:    'Hi' -> '72 105'")
    print()
    
    print("1. Text to Binary")
    print("2. Binary to Text")
    print("3. Text to Hex")
    print("4. Hex to Text")
    print("5. Decimal to Text")
    
    choice = input("\nChoice: ").strip()
    
    if choice == "1":
        text = input("Text: ")
        print(f"\nBinary: {text_to_binary(text)}")
    elif choice == "2":
        binary = input("Binary: ")
        print(f"\nText: {binary_to_text(binary)}")
    elif choice == "3":
        text = input("Text: ")
        print(f"\nHex: {text_to_hex(text)}")
    elif choice == "4":
        hex_str = input("Hex: ")
        print(f"\nText: {hex_to_text(hex_str)}")
    elif choice == "5":
        dec_str = input("Decimal: ")
        print(f"\nText: {decimal_to_text(dec_str)}")

if __name__ == "__main__":
    main()
