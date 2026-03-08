#!/usr/bin/env python3
"""
Expense Tracker
Track your spending. Stay on budget.
"""
import json
import os
from datetime import datetime

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
        category = input("Category (food/transport/entertainment/other): ").strip()
        description = input("Description: ").strip()
        
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        
        expenses.append(expense)
        print(f"✓ Added: {amount} for {category}")
        
    except ValueError:
        print("Invalid amount!")

def show_summary(expenses):
    if not expenses:
        print("No expenses yet!")
        return
    
    total = sum(e["amount"] for e in expenses)
    
    print(f"\n💰 Total: ${total:.2f}")
    print(f"📊 Number of expenses: {len(expenses)}")
    
    # By category
    categories = {}
    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]
    
    print("\nBy Category:")
    for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: ${amount:.2f}")

def main():
    print("\n💸 EXPENSE TRACKER 💸")
    print("=" * 40)
    
    expenses = load_expenses()
    
    print("Commands: add, summary, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "quit" or cmd == "q":
            save_expenses(expenses)
            break
        elif cmd == "add" or cmd == "a":
            add_expense(expenses)
            save_expenses(expenses)
        elif cmd == "summary" or cmd == "s":
            show_summary(expenses)
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
