#!/usr/bin/env python3
"""
Unit Converter
Convert between different units.
"""
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def main():
    print("\n📏 UNIT CONVERTER 📏")
    print("=" * 40)
    print("1. Celsius <-> Fahrenheit")
    print("2. Kilometers <-> Miles")
    print("3. Kilograms <-> Pounds")
    
    try:
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            c = float(input("Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")
        elif choice == "2":
            km = float(input("Kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == "3":
            kg = float(input("Kilograms: "))
            print(f"{kg} kg = {kg_to_pounds(kg):.2f} pounds")
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
