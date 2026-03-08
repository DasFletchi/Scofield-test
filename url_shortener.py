#!/usr/bin/env python3
"""
URL Shortener - Local
Just stores links locally. Not a real shortener.
"""
import json
import os
import random
import string

LINKS_FILE = "shortened_links.json"

def load_links():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_links(links):
    with open(LINKS_FILE, 'w') as f:
        json.dump(links, f, indent=2)

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def shorten(url, links):
    code = generate_short_code()
    while code in links:
        code = generate_short_code()
    
    links[code] = url
    short_url = f"http://s.co/{code}"
    return short_url

def expand(code, links):
    if code in links:
        return links[code]
    return None

def main():
    print("\n🔗 URL SHORTENER (Local) 🔗")
    print("=" * 40)
    
    links = load_links()
    
    print("Commands: shorten, expand, list, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "quit" or cmd == "q":
            break
        elif cmd == "shorten" or cmd == "s":
            url = input("URL: ").strip()
            if url:
                short = shorten(url, links)
                save_links(links)
                print(f"Short URL: {short}")
        elif cmd == "expand" or cmd == "e":
            code = input("Code: ").strip()
            url = expand(code, links)
            if url:
                print(f"Original: {url}")
            else:
                print("Not found!")
        elif cmd == "list" or cmd == "l":
            if links:
                print("\nSaved Links:")
                for code, url in links.items():
                    print(f"  {code} -> {url}")
            else:
                print("No links saved!")
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
