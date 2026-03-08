#!/usr/bin/env python3
"""
Task Manager - Simple CLI Todo List
Because even geniuses need to remember what to do.
"""
import json
import os
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    print(f"✓ Added: {task}")

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n📋 Your Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⬜"
        print(f"{i}. {status} {t['task']}")

def complete_task(tasks, num):
    if 0 < num <= len(tasks):
        tasks[num-1]["done"] = True
        print(f"✓ Completed: {tasks[num-1]['task']}")
    else:
        print("Invalid task number")

def delete_task(tasks, num):
    if 0 < num <= len(tasks):
        deleted = tasks.pop(num-1)
        print(f"🗑️ Deleted: {deleted['task']}")
    else:
        print("Invalid task number")

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        list_tasks(tasks)
        print("\nUsage: python todo.py <add|list|done|delete> [task]")
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_tasks(tasks)
    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo.py add <task>")
            return
        task = " ".join(sys.argv[2:])
        add_task(tasks, task)
        save_tasks(tasks)
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: python todo.py done <number>")
            return
        try:
            num = int(sys.argv[2])
            complete_task(tasks, num)
            save_tasks(tasks)
        except ValueError:
            print("Please provide a valid number")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python todo.py delete <number>")
            return
        try:
            num = int(sys.argv[2])
            delete_task(tasks, num)
            save_tasks(tasks)
        except ValueError:
            print("Please provide a valid number")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
