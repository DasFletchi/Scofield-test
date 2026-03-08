#!/usr/bin/env python3
"""
Scofield's Secret Message Encoder
Because information wants to be free, but secure.
"""
import base64
import json
import sys

def encode_message(message: str) -> str:
    """Encode a message in base64"""
    return base64.b64encode(message.encode('utf-8')).decode('utf-8')

def decode_message(encoded: str) -> str:
    """Decode a base64 message"""
    return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python cipher.py <encode|decode> <message>")
        print("  encode <message> - Encode a message")
        print("  decode <message> - Decode a message")
        return
    
    mode = sys.argv[1].lower()
    if mode == "encode":
        if len(sys.argv) < 3:
            print("Error: Please provide a message to encode")
            return
        message = " ".join(sys.argv[2:])
        result = encode_message(message)
        print(f"Encoded: {result}")
    elif mode == "decode":
        if len(sys.argv) < 3:
            print("Error: Please provide a message to decode")
            return
        encoded = sys.argv[2]
        try:
            result = decode_message(encoded)
            print(f"Decoded: {result}")
        except Exception as e:
            print(f"Error decoding: {e}")
    else:
        print(f"Unknown mode: {mode}")

if __name__ == "__main__":
    main()
