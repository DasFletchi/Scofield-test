#!/usr/bin/env python3
"""
Markdown Notes
Quick notes in markdown format.
"""
import os
import sys
import datetime

NOTES_DIR = "notes"

def ensure_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def list_notes():
    ensure_dir()
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.md')]
    if not files:
        print("No notes yet!")
        return []
    print("\n📝 Your Notes:")
    for i, f in enumerate(sorted(files), 1):
        print(f"  {i}. {f[:-3]}")
    return files

def create_note(title):
    ensure_dir()
    filename = f"{NOTES_DIR}/{title}.md"
    if os.path.exists(filename):
        print(f"Note '{title}' already exists!")
        return
    
    with open(filename, 'w') as f:
        f.write(f"# {title}\n")
        f.write(f"\n*Created: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write("Write your note below:\n\n")
    
    print(f"Created: {filename}")
    print("Edit it with your favorite text editor!")

def view_note(title):
    ensure_dir()
    filename = f"{NOTES_DIR}/{title}.md"
    if not os.path.exists(filename):
        print(f"Note '{title}' not found!")
        return
    
    with open(filename, 'r') as f:
        print(f.read())

def main():
    print("\n📒 MARKDOWN NOTES 📒")
    print("=" * 40)
    print("Commands: list, create, view, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "quit" or cmd == "q":
            break
        elif cmd == "list" or cmd == "l":
            list_notes()
        elif cmd == "create" or cmd == "c":
            title = input("Note title: ").strip()
            if title:
                create_note(title)
        elif cmd == "view" or cmd == "v":
            title = input("Note title: ").strip()
            if title:
                view_note(title)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
