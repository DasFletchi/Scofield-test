#!/usr/bin/env python3
"""
BMI Calculator
Because health matters, even in prison.
"""
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("\n⚖️ BMI CALCULATOR ⚖️")
    print("=" * 40)
    
    try:
        weight = float(input("Weight (kg): "))
        height = float(input("Height (cm): "))
        
        if weight <= 0 or height <= 0:
            print("Please enter positive values!")
            return
        
        height_m = height / 100
        bmi = calculate_bmi(weight, height_m)
        category = get_category(bmi)
        
        print(f"\nYour BMI: {bmi:.1f}")
        print(f"Category: {category}")
        
        print("\n📊 BMI Categories:")
        print("  < 18.5   - Underweight")
        print("  18.5-24.9 - Normal")
        print("  25-29.9  - Overweight")
        print("  30+      - Obese")
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
