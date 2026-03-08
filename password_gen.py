#!/usr/bin/env python3
"""
Password Generator
Generate secure passwords. Because security matters.
"""
import random
import string
import sys

def generate_password(length=16, use_special=True):
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    
    if use_special:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    while len(password) < length:
        password.append(random.choice(chars))
    
    random.shuffle(password)
    return ''.join(password)

def main():
    print("\n🔐 PASSWORD GENERATOR 🔐")
    print("=" * 40)
    
    try:
        length = int(input("Password length (default 16): ") or "16")
        use_special = input("Use special chars? (Y/n): ").lower() != 'n'
        
        print("\nGenerating...")
        
        passwords = []
        for _ in range(5):
            passwords.append(generate_password(length, use_special))
        
        print("\n📋 Your passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"  {i}. {pwd}")
            
        print("\n💡 Pro tip: Use a password manager!")
        
    except ValueError:
        print("Please enter a valid number!")
    except KeyboardInterrupt:
        print("\n\nCancelled.")

if __name__ == "__main__":
    main()
